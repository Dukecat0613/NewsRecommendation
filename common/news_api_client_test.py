# @Author: Dukecat
# @Date:   2017-05-02T23:27:09-04:00
# @Last modified by:   Dukecat
# @Last modified time: 2017-05-11T19:42:25-04:00





import news_api_client as client

def test_basic():
    news = client.getNewsFromSource()
    assert len(news) > 0
    news = client.getNewsFromSource(sources=['bbc-news'])
    assert len(news) > 0
    print 'test_basic passed!'

if __name__ == "__main__" :
    test_basic()
