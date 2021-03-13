from flask import Flask, request
from flask_restx import Resource, Api
from pymongo import MongoClient
import datetime
from outbreak_location import location_filter
from outbreak_time import time_filter
from outbreak_disease import disease_filter
from json import dumps

client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details

print(type(col))
#location = request.args.get('location')
#dtime = request.args.get('date')
#disease = request.args.get('disease')
# remove this when we get everything together
x = datetime.datetime(2020,2,28)
newcol = location_filter("China", col)
newcol = time_filter(x, newcol)
