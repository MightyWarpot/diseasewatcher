import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
from flask import Flask, request
from flask_restx import Resource, Api
from pymongo import MongoClient
import datetime
import re
from outbreak_location import location_filter
from outbreak_time import time_filter
from outbreak_disease import disease_filter
from outbreak_region import region_filter
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
@api.doc(params={'location' :'Country', 
                'disease' : "Type of Disease", 
                'date': 'Date of article',
                'region': 'Region of article'})
class endpoint(Resource):   
    def get(self):
        location = request.args.get('location', default = '')
        disease = request.args.get('disease', default = '')
        time = request.args.get('time', default = '')
        region = requests.arg.get('region', default = '')
        if (time != ''):
            
            day = int(time[0:2])
            month = int(time[2:4])
            year = int(time[4:8])

            dtime = datetime.datetime(year, month, day)
            year = dtime.strftime("%Y")
            month = dtime.strftime("%B")
            time = month + " " + str(day) + ", " + year
        else:
            dtime = ''

        print(time)
        time_results = time_filter(time, col)
        
        location_results = location_filter(location, col)


        # print(location_results[0])
        # print(location_results[1])


        disease_results = disease_filter(disease, col)

        region_results = region_filter(region, col)

        combined = location_results + disease_results + time_results + region_results

        combined_filtered = []

        if location == '':
            location = "\w"
        if disease == '':
            disease = "\w"
        if time == '':
            time == "\w"
        if region == '':
            time == "\w"
        #temp_location == regexmatch everything

        for entry in combined:
            if (re.search(location, entry['location']) and
                re.search(disease, entry['disease']) and 
                re.search(time, entry['date']) and
                re.search(region, entry['region'])):

                combined_filtered.append(entry)


            # if (entry['location'] == location and
            #     entry['disease'] == disease):
            #     combined_filtered.append(entry)


        # print(combined_filtered)

        combined_filtered = [dict(t) for t in {tuple(d.items()) for d in combined_filtered}]

        return dumps(combined_filtered)




        # print(disease_results[0])
        # dtime = request.args.get('date')






def run():
    app.run(port=8000, debug=True)
