# database.py

import pymongo

def connect():
    """Connects to MongoDB"""
    client = pymongo.MongoClient("localhost", 27017)
    db = client["smartgrid"]
    return db

def insert_data(db,record):
    result = db.grid.insert(record)  # W1514: deprecated insert()
    print("Data inserted")  # W1203: logging should be used instead of print
    return result
