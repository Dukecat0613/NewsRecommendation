# @Author: Dukecat
# @Date:   2017-05-02T23:27:09-04:00
# @Last modified by:   Dukecat
# @Last modified time: 2017-05-11T19:42:22-04:00





import pyjsonrpc

URL = "http://localhost:6060/"

client = pyjsonrpc.HttpClient(url=URL)

def classify(text):
    topic = client.call('classify', text)
    print "Topic: %s" % str(topic)
    return topic
