
from datetime import datetime

from logging import FileHandler, INFO, basicConfig, DEBUG

from json import dumps
# from API_Source_Code.src.outbreak_all import disease_all
# from API_Source_Code.src.outbreak_region import region_filter
# from API_Source_Code.src.outbreak_disease import disease_filter
# from API_Source_Code.src.outbreak_time import time_filter
# from API_Source_Code.src.outbreak_location import location_filter
import sys
sys.path.append('C:\\Python38\\Lib\\site-packages')
import os 
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
sys.path.append('...')
sys.path.append('../../')
sys.path.append('../../../')
sys.path.append('../../../../')
sys.path.append('C:\\Python38\\Lib\\site-packages')
from flask import Flask, request
from flask_restx import Resource, Api, abort, fields
from pymongo import MongoClient
from datetime import *
from flask_cors import CORS
import re
#from API_Source_Code.src.outbreak_location import location_filter
#from API_Source_Code.src.outbreak_time import time_filter
#from API_Source_Code.src.outbreak_disease import disease_filter
#from API_Source_Code.src.outbreak_region import region_filter
#from API_Source_Code.src.outbreak_all import disease_all
from outbreak_location import location_filter
from outbreak_time import time_filter
from outbreak_disease import disease_filter
from outbreak_region import region_filter
from outbreak_all import disease_all
app = Flask(__name__)
api = Api(app)
CORS(app)
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
                'disease' : "Type of Disease (e.g. Cholera)", 
                'start date': 'Outbreak reported on or after this date (dd/mm/yyyy)',
                'end date': 'Outbreak reported on or before this date (dd/mm/yyyy)',
                'region': 'Geographic region of outbreak (e.g. Europe)',
                'start_index': 'Articles start from this index (Default is 0 which is the first article)',
                'end_index': 'Articles end at this index (Default is len(articles) - 1 which is the last article)',
                 })
class endpoint(Resource):
    @api.response(200, 'Success', article)

    @api.response(400, 'Bad request', error_msg)
    @api.response(404, 'URL not found')
    @api.response(500, 'Internal Server Error')
    @api.doc(description='''Retrieves articles from outbreaknewstoday.com based on location, disease, time period, region.
        User can also specify how many results they would like to see.
        "location" or "disease" or "region" is required and date must be in the format 'dd/mm/yyyy'. By default all results are returned. 
        Allowable inputs for "region": 'Africa', 'Asia', 'Australia', 'Canada', 'Europe', 'Indian subcontinent', 'Latin America and the Caribbean', 'Middle East',  'US News'.
        Return object is a list of dictionaries with title, date, location, region, url, disease and body of the article.
        Semantics of location, region, etc. are detailed below.
    
        ''')

    def get(self):
        location = request.args.get('location', default = '').strip()
        disease = request.args.get('disease', default = '').strip()
        startdate = request.args.get('start date', default = '').strip()
        enddate = request.args.get('end date', default = '').strip()
        region = request.args.get('region', default = '').strip()
        end_index = request.args.get('end_index', default = '').strip()
        start_index = request.args.get('start_index', default='').strip()
        if (not re.match('^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$', startdate) and startdate != ''):                                 
            abort(400, "Start date is incorrectly formatted")
        if (not re.match('^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$', enddate) and enddate != ''):                    
            abort(400, "End date is incorrectly formatted")
        max_len = col.count_documents({})
        if(location == '' and disease == '' and region == ''):
            abort(400, "Location, region and disease cannot all be empty")
       
       
  

        if (startdate != ''):
            
            startdateArray = startdate.split("/")
            day = int(startdateArray[0])
            month = int(startdateArray[1])
            year = int(startdateArray[2])

            startdtime = datetime(year, month, day)
        else:
            startdtime = ''

        if (enddate != ''):
            enddateArray = enddate.split("/")
            day = int(enddateArray[0])
            month = int(enddateArray[1])
            year = int(enddateArray[2])

            enddtime = datetime(year, month, day)
        else:
            enddtime = ''

        #Get results by searching mongodb datebase
        time_results = time_filter(startdtime, enddtime, col)

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
        if region == '':
            region == "\w"
        if startdtime == '': 
            startdtime = datetime(1,1,1)
        if enddtime == '':
            enddtime = datetime(4000,1,1)
        
        #Filter results using regex such that the fields match user input
        for entry in combined:
            entrydate = datetime.strptime(entry['date'].strip(), '%B %d, %Y')
            if (re.search(location, entry['location']) and
                re.search(disease, entry['disease']) and 
                startdtime <= entrydate and
                entrydate <= enddtime and 
                re.search(region, entry['region'])):

                combined_filtered.append(entry)
        #Code to remove duplicates
        combined_filtered = [dict(t) for t in {tuple(d.items()) for d in combined_filtered}]

        matches_total = len(combined_filtered)
        if (combined_filtered == []):
            return []
        if start_index == '':
            start = 0
        else:
            try:
                start = int(start_index)
            except:
                abort(400, 'start index must be integer')

            if(start >= matches_total):
                abort(400, 'invalid starting index, exceeds number of results')
            if(start < 0):
                abort(400, 'starting index >= 0')
        if end_index == '':
            end = matches_total - 1
        else:
            try:
                end = int(end_index)
            except:
                abort(400, 'end_index must be integer')

            if( end >= matches_total):
                abort(400, 'invalid end_index, exceeds number of results')
            if( end < 0):
                abort(400, 'end_index  must be >= 0')

        
        if start_index != '' and end_index != '':
            if start_index > end_index:
                abort(400, 'start_index cannot be greater than end_index')

        return combined_filtered[start:end+1]
            # return combined_filtered[:int(results)]


file_handler = FileHandler('simple.log')
file_handler.setLevel(INFO)

prev_time = datetime.now()
@app.before_request
def log_info():
	app.logger.info('Original query data : %s', request.args.get)

@app.after_request
def log_response(response):
	now = datetime.now()
	op_time = now - prev_time
	app.logger.info('Query took ' + str(op_time.microseconds/1000) + ' milliseconds')
	app.logger.info('Response sent: %s', response.status_code)
	app.logger.info('Response sent: %s', response.get_json())
	return response

app.logger.addHandler(file_handler)
basicConfig(filename='detailed.log', level=DEBUG) 

if __name__ == "__main__":
    app.run(port=8000, debug=True)

