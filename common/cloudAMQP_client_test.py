# @Author: Dukecat
# @Date:   2017-05-02T23:27:09-04:00
# @Last modified by:   Dukecat
# @Last modified time: 2017-05-11T18:56:54-04:00





from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://gjyuvcic:mSQXnhxGAsV21bLs0-lsFSQ1Z6cSI2bC@clam.rmq.cloudamqp.com/gjyuvcic"

TEST_QUEUE_NAME = 'TEST_QUEUE'

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)

    sentMsg = {"test": "demo"}
    client.sendMessage(sentMsg)
    client.sleep(10)
    receivedMsg = client.getMessage()
    assert sentMsg == receivedMsg
    print 'test_basic passed!'

if __name__ == "__main__":
    test_basic()
