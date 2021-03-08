from flask import Flask, request
from flask_restx import Resource, Api
from pymongo import MongoClient
import datetime
import re
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
        disease = request.args.get('disease')


        location_results = location_filter(location, col)




        print(location_results[0])
        print(location_results[1])


        disease_results = disease_filter(disease, col)



        combined = location_results + disease_results
        print(type(combined))

        combined_filtered = []

        for entry in combined:
            if (entry['location'] == location and
                entry['disease'] == disease):
                combined_filtered.append(entry)


        # print(combined_filtered)


        # return dumps(combined_filtered)




        # print(disease_results[0])
        # dtime = request.args.get('date')






if __name__ == "__main__":
    app.run(port=0, debug=True)
