from powerpulse_etl.mongo_store import store_to_mongo
from unittest.mock import patch
import pymongo

@patch("powerpulse_etl.mongo_store.pymongo.MongoClient")
def test_inserting_into_mongo(mock_get):
    test_data = [{"stateId": "TX", "period": "2023"}]
    store_to_mongo(test_data)
    db = mock_get.return_value["powerpulse_etl"]
    collection = db["powerpulseETL"]
    assert collection.insert_many.called