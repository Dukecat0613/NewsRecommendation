import json
import os
import pickle
import random
import redis
import sys
import time

from bson.json_util import dumps
from datetime import datetime
from kafka import KafkaProducer

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import mongodb_client # defined get_db() that return the db from a certatin host:port
import news_recommendation_service_client
import parameters

REDIS_PORT = parameters.redisPort

NEWS_TABLE_NAME = parameters.NEWS_TABLE_NAME
CLICK_LOGS_TABLE_NAME = parameters.CLICK_LOGS_TABLE_NAME

NEWS_LIMIT = parameters.NEWS_LIMIT
NEWS_LIST_BATCH_SIZE = parameters.NEWS_LIST_BATCH_SIZE
USER_NEWS_TIME_OUT_IN_SECONDS = parameters.USER_NEWS_TIME_OUT_IN_SECONDS


redis_client = redis.StrictRedis(parameters.redisHost, REDIS_PORT, db=0)
Log_kafka_producer = KafkaProducer(bootstrap_servers = parameters.KAFKA_SERVER)


def getNewsSummariesForUser(user_id, page_num):
    """
    If the input user_id exists in Redis(cache in mem) then we 
    calculate his digested news; if cannot find in Redis (a new user), 
    then we get the most recent news records from MongoDB and set 
    100 most recent news as the his initial digested news and save in Redis.

    From Web Server:5050 call pyjsonrpc for the list of preference
    of a user, and set the first element in the list as the top 
    preference

    Delete the text field for saving bandwidth, in the meanwhile 
    set the 'reason' field to 'Recommend' if the 'class' field 
    shows as topPrefrence; set the 'time' field to 'today' if the
    'publishAt' shows the data is equal to today
    """
    page_num = int(page_num)
    begin_index = (page_num - 1) * NEWS_LIST_BATCH_SIZE
    end_index = page_num * NEWS_LIST_BATCH_SIZE

    # The final list of news to be returned.
    sliced_news = []

    if redis_client.get(user_id) is not None:
        news_digests = pickle.loads(redis_client.get(user_id)) # GET the corresponding (VALUE)news_id by (KEY)a user_id

        # If begin_index is out of range, this will return empty list;
        # If end_index is out of range (begin_index is within the range), this
        # will return all remaining news ids.
        sliced_news_digests = news_digests[begin_index:end_index]
        print sliced_news_digests
        db = mongodb_client.get_db()
        sliced_news = list(db[NEWS_TABLE_NAME].find({'digest':{'$in':sliced_news_digests}}))
    else:
        db = mongodb_client.get_db()
        total_news = list(db[NEWS_TABLE_NAME].find().sort([('publishedAt', -1)]).limit(NEWS_LIMIT)) # sort in descending order(-1)
        total_news_digests = map(lambda x:x['digest'], total_news)

        redis_client.set(user_id, pickle.dumps(total_news_digests))
        redis_client.expire(user_id, USER_NEWS_TIME_OUT_IN_SECONDS)

        sliced_news = total_news[begin_index:end_index]

    # Get preference for the user
    preference = news_recommendation_service_client.getPreferenceForUser(user_id)
    topPreference = None

    if preference is not None and len(preference) > 0:
        topPreference = preference[0]

    for news in sliced_news:
        # Remove text field to save bandwidth.
        del news['text']
        if news['class'] == topPreference:
            news['reason'] = 'Recommend'
        if news['publishedAt'].date() == datetime.today().date():
            news['time'] = 'today'
    return json.loads(dumps(sliced_news))

def logNewsClickForUser(user_id, news_id):
    message = {'userId': user_id, 'newsId': news_id, 'timestamp': datetime.utcnow()}

    db = mongodb_client.get_db()
    db[CLICK_LOGS_TABLE_NAME].insert(message)

    # Send log task to machine learning service for prediction
    message = {'userId': user_id, 'newsId': news_id}
    Log_kafka_producer.send(topic = parameters.LOG_CLICKS_TASK_QUEUE, value = json.dumps(message), timestamp_ms = time.time())
