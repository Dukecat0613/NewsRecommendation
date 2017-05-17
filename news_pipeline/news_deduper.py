import datetime
import os
import sys
import time
import json

from dateutil import parser
from sklearn.feature_extraction.text import TfidfVectorizer

from kafka import KafkaConsumer

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import mongodb_client
import news_topic_modeling_service_client
import parameters

SLEEP_TIME_IN_SECONDS = 1

NEWS_TABLE_NAME = parameters.NEWS_TABLE_NAME

SAME_NEWS_SIMILARITY_THRESHOLD = parameters.SAME_NEWS_SIMILARITY_THRESHOLD

Deque_kafka_consumer = KafkaConsumer(parameters.DEDUPE_NEWS_TASK_QUEUE, bootstrap_servers = parameters.KAFKA_SERVER)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict) :
        return
    task = msg
    text = str(task['text'].encode('utf-8'))
    if text is None:
        return

    # get all recent news based on publishedAt
    published_at = parser.parse(task['publishedAt'])
    published_at_day_begin = datetime.datetime(published_at.year, published_at.month, published_at.day, 0, 0, 0, 0)
    published_at_day_end = published_at_day_begin + datetime.timedelta(days=1)

    db = mongodb_client.get_db()
    same_day_news_list = list(db[NEWS_TABLE_NAME].find({'publishedAt': {'$gte': published_at_day_begin, '$lt': published_at_day_end}}))

    if same_day_news_list is not None and len(same_day_news_list) > 0:
        documents = [str(news['text'].encode('utf-8')) for news in same_day_news_list]
        documents.insert(0, text)

        # Calculate similarity matrix
        tfidf = TfidfVectorizer().fit_transform(documents)
        pairwise_sim = tfidf * tfidf.T

        print pairwise_sim.A

        rows, _ = pairwise_sim.shape

        for row in range(1, rows):
            if pairwise_sim[row, 0] > SAME_NEWS_SIMILARITY_THRESHOLD:
                # Duplicated news. Ignore.
                print "Duplicated news. Ignore."
                return

    task['publishedAt'] = parser.parse(task['publishedAt'])

    # Classify news
    title = task['title']
    if title is not None:
        topic = news_topic_modeling_service_client.classify(title)
        task['class'] = topic

    db[NEWS_TABLE_NAME].replace_one({'digest': task['digest']}, task, upsert=True)

for msg in Deque_kafka_consumer:
    if msg is not None:
        # Parse and process the task
        try:
            handle_message(json.loads(sg.value))
        except Exception as e:
            print e
            pass
    time.sleep(SLEEP_TIME_IN_SECONDS)
