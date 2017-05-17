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
