import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
from flask import Flask, request
from flask_restx import Resource, Api, abort
from pymongo import MongoClient
import datetime
import re
from outbreak_location import location_filter
from outbreak_time import time_filter
from outbreak_disease import disease_filter
from outbreak_region import region_filter
from outbreak_all import disease_all
from json import dumps
app = Flask(__name__)
api = Api(app)

#Connect to database
client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details


api = api.namespace('outbreak', description='Outbreak Reports Service')
@api.route('/')
@api.doc(params={'location' :'Country', 
                'disease' : "Type of Disease", 
                'date': 'Date of article',
                'region': 'Region of article',
                'results': 'Number of results'})
class endpoint(Resource):
    @api.response(200, 'Success')   

    def get(self):

        location = request.args.get('location', default = '')
        disease = request.args.get('disease', default = '')
        time = request.args.get('time', default = '')
        region = request.args.get('region', default = '')
        results = request.args.get('results', default = '')


        max_len = col.count_documents({})


        if(location == '' and disease == '' and time == ''
            and region == ''):

            all_res = disease_all(col)

            if results == '':
                return all_res

            elif results != '':
                try:
                    results = int(results)
                except:
                    abort(400, 'number of articles must be integer')

            if(results > max_len):
                abort(400, 'invalid number of articles, exceeds amount stored in DB')

            #Set behaviour if user inputs 0
            if(results == 0):
                abort(400, 'number of articles > 0')

            else:
                return all_res[:results]


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

        #Get results by searching mongodb datebase
        time_results = time_filter(time, col)
        
        location_results = location_filter(location, col)

        disease_results = disease_filter(disease, col)

        region_results = region_filter(region, col)

        combined = location_results + disease_results + time_results + region_results

        combined_filtered = []

        #if no user input set variable as regex expression to match any string
        if location == '':
            location = "\w"
        if disease == '':
            disease = "\w"
        if time == '':
            time == "\w"
        if region == '':
            time == "\w"

        #Filter results using regex such that the fields match user input
        for entry in combined:
            if (re.search(location, entry['location']) and
                re.search(disease, entry['disease']) and 
                re.search(time, entry['date']) and
                re.search(region, entry['region'])):

                combined_filtered.append(entry)



        #Code to remove duplicates
        combined_filtered = [dict(t) for t in {tuple(d.items()) for d in combined_filtered}]

        if(results == ''):
            return combined_filtered
        else:
            # print(results)
            return combined_filtered[:int(results)]

if __name__ == "__main__":
    app.run(port=8000, debug=True)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
