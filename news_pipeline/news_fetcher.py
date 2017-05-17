# -*- coding: utf-8 -*-

import os
import sys
import json
import time

from kafka import KafkaConsumer, KafkaProducer

from newspaper import Article

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

import cnn_news_scraper
import parameters

SLEEP_TIME_IN_SECONDS = 1

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)
Deque_kafka_producer = KafkaProducer(bootstrap_servers = parameters.KAFKA_SERVER)
Scrape_kafka_consumer = KafkaConsumer(parameters.SCRAPE_NEWS_TASK_QUEUE, bootstrap_servers = parameters.KAFKA_SERVER)

def handle_message(msg):
    if msg is None or not isinstance(msg, dict):
        print 'message is broken'
        return

    task = msg
    ''' Below is using xPath'''
    # text = None
    #
    # #we support cnn only num_of_new_news
    # if task['source'] == 'cnn':
    #     print 'Scraping CNN news'
    #     text = cnn_news_scraper.extract_news(task['url'])
    # else:
    #     print 'News source [%s] is not supported.' % task['source']
    #
    # task['text'] = text
    # dedupe_news_queue_client.sendMessage(task)

    article = Article(task['url'])
    article.download()
    article.parse()

    print article.text

    task['text'] = article.text

    Deque_kafka_producer.send(topic = parameters.DEDUPE_NEWS_TASK_QUEUE, value = json.dumps(task), timestamp_ms=time.time())

for msg in Scrape_kafka_consumer:
    if msg is not None:
        # Handle message
        try:
            handle_message(msg)
        except Exception as e:
            print e
            pass
    time.sleep(SLEEP_TIME_IN_SECONDS)
