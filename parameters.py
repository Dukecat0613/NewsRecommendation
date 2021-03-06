redisHost = 'ec2-52-205-251-116.compute-1.amazonaws.com'
redisPort = 6380
NEWS_TABLE_NAME = "newCollection"
CLICK_LOGS_TABLE_NAME = 'click_logs'
NEWS_LIMIT = 100
NEWS_LIST_BATCH_SIZE = 10
USER_NEWS_TIME_OUT_IN_SECONDS = 600
NEWS_TIME_OUT_IN_SECONDS = 3600 * 24
SLEEP_TIME_IN_SECONDS = 10

## Kafka Topic
DEDUPE_NEWS_TASK_QUEUE = 'DEDUPE'
SCRAPE_NEWS_TASK_QUEUE = 'SCRAPE'
LOG_CLICKS_TASK_QUEUE = 'LOG'

Service_SERVER_PORT = 4040
KAFKA_SERVER = ['ec2-54-163-153-215.compute-1.amazonaws.com:9092', 'ec2-52-207-212-20.compute-1.amazonaws.com:9092']

PREFERENCE_MODEL_TABLE_NAME = "user_preference_model"
Recommendation_SERVER_PORT = 5050

SAME_NEWS_SIMILARITY_THRESHOLD = 0.9

SERVER_HOST = 'ec2-54-175-248-107.compute-1.amazonaws.com'

MONGO_DB_HOST = 'ec2-52-205-251-116.compute-1.amazonaws.com'
MONGO_DB_PORT = 33333
DB_NAME = 'RecommendationNews'
