import pytest
from API_Source_Code.src.outbreak_region import region_filter
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details


def test_outbreak_location_basecase():
    res = region_filter('Asia', col)
    for entry in res:
        assert entry['region'] == 'Asia'
