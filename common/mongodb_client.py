from pymongo import MongoClient
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import parameters

MONGO_DB_HOST = parameters.MONGO_DB_HOST
MONGO_DB_PORT = parameters.MONGO_DB_PORT
DB_NAME = parameters.DB_NAME

client = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))

def get_db(db = DB_NAME):
    db = client[db]
    return db
