import pytest
from API_Source_Code.src.outbreak_disease import disease_filter
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details


def test_outbreak_location_basecase():
    res = disease_filter('COVID-19', col)
    for entry in res:
        assert entry['disease'] == 'COVID-19'
