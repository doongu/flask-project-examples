from pymongo import MongoClient
connection = MongoClient()

connection = MongoClient('localhost', 27017)
connection = MongoClient('mongodb://localhost:27017/')

print(connection)