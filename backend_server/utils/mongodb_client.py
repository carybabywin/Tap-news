""" Mongodb client """
from pymongo import MongoClient

MONGO_DB_HOST = 'localhost'
MONGO_DB_PORT = '27017'
DB_NAME = 'tap-news'

CLIENT = MongoClient("%s:%s" % (MONGO_DB_HOST, MONGO_DB_PORT))
# return database
def get_db(database=DB_NAME):
    """ return database """
    return CLIENT[database]

