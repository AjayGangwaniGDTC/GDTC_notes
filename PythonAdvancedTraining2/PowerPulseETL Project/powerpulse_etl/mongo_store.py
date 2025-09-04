'''This file is used to load the data from the api into mongoDB database'''

import pymongo
from .config import MONGO_URI, logger
from .decorators import log_phase

@log_phase("MongoDB Store")
def store_to_mongo(data):
    '''function to connect mongoDB and then inserting the values if connection 
    successful'''
    #create a client object to get connected with mongo client
    client = pymongo.MongoClient(MONGO_URI)
    #get list of database available on connection url
    db = client["powerpulse_etl"]
    #we choose the database from client connection
    collection = db["powerpulseETL"]
    #Inserting the values into the database with table
    result = collection.insert_many(data)
    logger.info("Inserted %s records into MongoDB.", len(result.inserted_ids))
    client.close()
