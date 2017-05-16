# @Author: Hang Wu <Dukecat>
# @Date:   2017-05-16T14:46:18-04:00
# @Email:  wuhang0613@gmail.com
# @Filename: backfill.py
# @Last modified by:   Dukecat
# @Last modified time: 2017-05-16T16:11:54-04:00



import os
import sys

# import common package in parent directory
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'common'))

import mongodb_client
import news_topic_modeling_service_client

if __name__ == '__main__':
    db = mongodb_client.get_db()
    cursor = db['news'].find({})
    count = 0
    for news in cursor:
        count += 1
        print count
        if 'class' not in news:
            print 'Populating classes...'
            title = news['title']
            topic = news_topic_modeling_service_client.classify(title)
            news['class'] = topic
            db['news'].replace_one({'digest': news['digest']}, news, upsert=True)
