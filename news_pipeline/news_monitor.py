# -*- coding: utf-8 -*-

from kafka import KafkaProducer
# from kafka.errors import KafkaError, KafkaTimeoutError

import datetime
import hashlib
import os
import redis
import sys
import json
import time

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import parameters
import news_api_client

NEWS_SOURCES = [
    'bbc-news',
    'bbc-sport',
    'bloomberg',
    'cnn',
    'entertainment-weekly',
    'espn',
    'ign',
    'techcrunch',
    'the-new-york-times',
    'the-wall-street-journal',
    'the-washington-post'
]

redis_client = redis.StrictRedis(parameters.redisHost, parameters.redisPort)
Monitor_kafka_producer = KafkaProducer(bootstrap_servers = parameters.KAFKA_SERVER)

while True:
    news_list = news_api_client.getNewsFromSource(NEWS_SOURCES)

    num_of_new_news = 0
    print len(news_list)
    for news in news_list:
        news_digest = hashlib.md5(news['title'].encode('utf-8')).digest().encode('base64')

        # if redis_client.get(news_digest) is None:

        num_of_new_news += 1
        news['digest'] = news_digest

        if news['publishedAt'] is None:
                # format: YYYY-MM-DDTHH:MM:SSZ in UTC
            news['publishedAt'] = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

        redis_client.set(news_digest, news)
        redis_client.expire(news_digest, parameters.NEWS_TIME_OUT_IN_SECONDS)

        Monitor_kafka_producer.send(topic=parameters.SCRAPE_NEWS_TASK_QUEUE, value=json.dumps(news), timestamp_ms=time.time())

    print "Fetched %d new news." % num_of_new_news

    time.sleep(parameters.SLEEP_TIME_IN_SECONDS)
