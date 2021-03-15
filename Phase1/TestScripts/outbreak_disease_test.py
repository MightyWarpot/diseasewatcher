import pytest
from API_Source_Code.src.outbreak_disease import disease_filter
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details


def test_outbreak_location_covid():
    res = disease_filter('COVID-19', col)
    for entry in res:
        assert entry['disease'] == 'COVID-19'


def test_outbreak_location_dengue():
    res = disease_filter('Dengue fever', col)
    for entry in res:
        assert entry['disease'] == 'Dengue fever'


def test_outbreak_location_measles():
    res = disease_filter('Measles', col)
    for entry in res:
        assert entry['disease'] == 'Measles'

def test_outbreak_location_noinput():
    res = disease_filter('', col)
    assert res == []

