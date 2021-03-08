from flask import Flask, request
from flask_restx import Resource, Api
from pymongo import MongoClient
import datetime
from outbreak_location import location_filter
from outbreak_time import time_filter
from outbreak_disease import disease_filter
from json import dumps
app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'

client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details

@api.route('/outbreak/')
class endpoint(Resource):   
    def get(self):
        location = request.args.get('location')
        dtime = request.args.get('date')
        disease = request.args.get('disease')
        # remove this when we get everything together
        newcol = location_filter(location, col)
        newcol = time_filter(dtime, newcol)
        newcol = disease_filter(disease, newcol)
        return dumps(res)


if __name__ == "__main__":
    app.run(port=0, debug=True)
