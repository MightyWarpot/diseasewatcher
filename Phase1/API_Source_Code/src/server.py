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
                'page': 'Page number'})
class endpoint(Resource):
    @api.response(200, 'Success')   

    def get(self):
        location = request.args.get('location', default = '')
        disease = request.args.get('disease', default = '')
        time = request.args.get('time', default = '')
        region = request.args.get('region', default = '')
        pageNo = request.args.get('page', default = '0')

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

        #Error for if user input is not integer
        try:
            pageNo = int(pageNo)
        except ValueError:
            print("Input must be integer")

        #Set behaviour if user inputs 0
        if(pageNo == 0):
            pageNo = 1


        #Calculate indices for array slicing in pagination
        page_start = 0
        page_end = 0
        if(pageNo != ''):
            page_end = pageNo*10
            page_start = page_end-10

        #Code to remove duplicates
        combined_filtered = [dict(t) for t in {tuple(d.items()) for d in combined_filtered}]

        if(page_start > len(combined_filtered)):
            raise ValueError('Invalid input')

        if(pageNo == ''):
            return dumps(combined_filtered)
        else:
            return dumps(combined_filtered[page_start:page_end])

if __name__ == "__main__":
    app.run(port=8000, debug=True)

if __name__ == "__main__":
    app.run(port=8000, debug=True)
