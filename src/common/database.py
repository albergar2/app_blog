import pymongo

__author__ = 'albergar2 '


class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None

    # This method is gonna belong to the whole class and not to an object
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client['blog_db']

    @staticmethod
    def insert(collection, data):
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query)