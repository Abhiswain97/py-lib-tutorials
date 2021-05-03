import pymongo
from pymongo import MongoClient

client = MongoClient("mongodb://127.0.0.1:27017")

db = client.acme

collection = db.posts

res = collection.find_one()

print(res)