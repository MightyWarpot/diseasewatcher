import pytest
from API_Source_Code.src.outbreak_all import disease_all
from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details

max_len = col.count_documents({})

def test_outbreak_all():
    res = disease_all(col)

    assert max_len == len(res)
