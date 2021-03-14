import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
from flask import Flask, request
from flask_restx import Resource, Api, abort, fields
from pymongo import MongoClient
import datetime
import re
from outbreak_location import location_filter
from outbreak_time import time_filter
from outbreak_disease import disease_filter
from outbreak_region import region_filter
from outbreak_all import disease_all
from json import dumps

import re
app = Flask(__name__)
api = Api(app)

#Connect to database
client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details
article_line = api.model('line', {
    "line": fields.String()
})
error_msg = api.model('error', {
    "message": fields.String(example="Date is incorrectly formatted")
})
article = api.model('article', {
    "title": fields.String(example="SARS, MERS ruled out in China pneumonia cluster"),
    "date": fields.String(example="January 5, 2020"),
    "location": fields.String(example="China"),
    "region": fields.String(example="Asia"),
    "url": fields.String(example="http://outbreaknewstoday.com/sars-mers-ruled-out-in-china-pneumonia-cluster-40965/"),
    "disease": fields.String(example="SARS"),
    "body": fields.List(fields.String(example="Health officials in the city of Wuhan in Hubei province, China ")),
  } )


api = api.namespace('outbreak', description='Outbreak Reports Service')
@api.route('/')
@api.doc(params={'location' :'Country or State/Province (e.g. China)', 
                'disease' : "Type of Disease (e.g. Ebola)", 
                'start date': 'Start date of article (dd/mm/yyyy)',
                'end date': 'End date of article (dd/mm/yyyy)',
                'region': 'Continent of outbreak (e.g. Europe)',
                'results': 'Number of results'})
class endpoint(Resource):
    @api.response(200, 'Success', article)
   
    @api.response(400, 'Bad request', error_msg)
    @api.response(500, 'Internal Server Error')
    @api.doc(description='''Retrieves articles from outbreaknewstoday.com based on location, disease, time period, region. 
        User can also specify how many results they would like to see.
        No fields are required but date must be in the format 'dd/mm/yyyy'. 
        Return object is a list of dictionaries with title, date, location, region, url, disease and body of the article.
        Semantics of location, region, etc. are detailed below.''')   

    def get(self):

        location = request.args.get('location', default = '')
        disease = request.args.get('disease', default = '')
        startdate = request.args.get('start date', default = '')
        enddate = request.args.get('end date', default = '')
        region = request.args.get('region', default = '')
        results = request.args.get('results', default = '')


        max_len = col.count_documents({})


        if(location == '' and disease == '' and startdate == ''
            and enddate == '' and region == ''):

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



        if (startdate != ''):
            
            startdateArray = startdate.split("/")
            day = startdateArray[0]
            month = startdateArray[1]
            year = startdateArray[2]

            startdtime = datetime.datetime(year, month, day)
        else:
            startdtime = ''

        if (enddate != ''):
            enddateArray = enddate.split("/")
            day = startdateArray[0]
            month = startdateArray[1]
            year = startdateArray[2]

            startdtime = datetime.datetime(year, month, day)
        else:
            startdtime = ''
        #Get results by searching mongodb datebase
        # time_results = time_filter(time, col)
        
        location_results = location_filter(location, col)

        disease_results = disease_filter(disease, col)

        region_results = region_filter(region, col)

        combined = location_results + disease_results + region_results

        combined_filtered = []

        #if no user input set variable as regex expression to match any string
        if location == '':
            location = "\w"
        if disease == '':
            disease = "\w"
        # if time == '':
        #     time == "\w"
        if region == '':
            region == "\w"

        #Filter results using regex such that the fields match user input
        for entry in combined:
            if (re.search(location, entry['location']) and
                re.search(disease, entry['disease']) and
                re.search(region, entry['region'])):
                # re.search(time, entry['date']) and


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


