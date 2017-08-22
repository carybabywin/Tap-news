from cloudAMQP_client import CloudAMQPClient

CLOUDAMQP_URL = "amqp://ppzavupv:S-gM7QCVgj5HkHUl1316RIfhJ2xWQATm@donkey.rmq.cloudamqp.com/ppzavupv"
TEST_QUEUE_NAME = "test"

def test_basic():
    client = CloudAMQPClient(CLOUDAMQP_URL, TEST_QUEUE_NAME)
    
    sentMsg = {"test":"test"}
    client.sendMessage(sentMsg)
    receivedMsg = client.getMessage()

    assert sentMsg == receivedMsg
    print "test_basic passed."

if __name__ == "__main__":
    test_basic()