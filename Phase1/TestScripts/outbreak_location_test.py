
import pytest
from API_Source_Code.src.outbreak_location import location_filter
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details



def test_outbreak_location_China():
    res = location_filter('China', col)
    for entry in res:
        assert entry['location'] == 'China'


def test_outbreak_location_Vietnam():
    res = location_filter('Vietnam', col)
    for entry in res:
        assert entry['location'] == 'Vietnam'


def test_outbreak_location_US():
    res = location_filter('US', col)
    for entry in res:
        assert entry['location'] == 'US'


def test_outbreak_location_noinput():
    res = location_filter('', col)
    assert res ==[]

