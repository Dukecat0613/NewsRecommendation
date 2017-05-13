# @Author: Dukecat
# @Date:   2017-05-02T23:27:09-04:00
# @Last modified by:   Dukecat
# @Last modified time: 2017-05-11T19:42:20-04:00





import news_topic_modeling_service_client as client

def test_basic():
    newsTitle = "Pentagon might propose ground troops for Syria"
    topic = client.classify(newsTitle)
    assert topic == "Politics & Government"
    print 'test_basic passed!'

if __name__ == "__main__":
    test_basic()
