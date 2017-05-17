# -*- coding: utf-8 -*-

import os
import sys

from newspaper import Article

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'scrapers'))

import cnn_news_scraper
from cloudAMQP_client import CloudAMQPClient

DEDUPE_NEWS_TASK_QUEUE_URL = "amqp://fdosrchl:tyNc2JFvHCi1WS9c5ohb5eEedF9rmtIz@crocodile.rmq.cloudamqp.com/fdosrchl"
DEDUPE_NEWS_TASK_QUEUE_NAME = "DEDUPE_NEWS_TASK_QUEUE"
SCRAPE_NEWS_TASK_QUEUE_URL = "amqp://qeioajkj:qJ0JdnU8_xQ9RVePRvPu14BdwqvvyXxT@salamander.rmq.cloudamqp.com/qeioajkj"
SCRAPE_NEWS_TASK_QUEUE_NAME = "SCRAPE_NEWS_TASK_QUEUE"

SLEEP_TIME_IN_SECONDS = 1

dedupe_news_queue_client = CloudAMQPClient(DEDUPE_NEWS_TASK_QUEUE_URL, DEDUPE_NEWS_TASK_QUEUE_NAME)
scrape_news_queue_client = CloudAMQPClient(SCRAPE_NEWS_TASK_QUEUE_URL, SCRAPE_NEWS_TASK_QUEUE_NAME)

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

    dedupe_news_queue_client.sendMessage(task)

while True:
    # fetch msg from queue
    if scrape_news_queue_client is not None:
        msg = scrape_news_queue_client.getMessage()
        if msg is not None:
            # Handle message
            try:
                handle_message(msg)
            except Exception as e:
                print e
                pass
        scrape_news_queue_client.sleep(SLEEP_TIME_IN_SECONDS)
