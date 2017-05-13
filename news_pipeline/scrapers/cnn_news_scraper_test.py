# @Author: Dukecat
# @Date:   2017-05-02T23:27:09-04:00
# @Last modified by:   Dukecat
# @Last modified time: 2017-05-11T19:42:34-04:00





import cnn_news_scraper as scraper

EXPECTED_STRING = "the man charged with killing five people at the Fort Lauderdale airport"
CNN_NEWS_URL = "http://edition.cnn.com/2017/01/17/us/fort-lauderdale-shooter-isis-claim/index.html"

def test_basic():
    news = scraper.extract_news(CNN_NEWS_URL)

    assert EXPECTED_STRING in news
    print news
    print 'test_basic passed!'

if __name__ ==  "__main__":
    test_basic()
