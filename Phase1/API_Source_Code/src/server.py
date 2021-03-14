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
from json import dumps
from logging import FileHandler, INFO, basicConfig, DEBUG
from datetime import datetime
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
                'date': 'Date of article (dd/mm/yyyy)',
                'region': 'Continent of outbreak (e.g. Europe)',
                'page': 'Page number'})
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
        time = request.args.get('date', default = '')
        region = request.args.get('region', default = '')
        pageNo = request.args.get('page', default = '0')
        print(time)
        if (not re.match('^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$', time) and time != ''):
                                    
            abort(400, "Date is incorrectly formatted")

        if (time != ''):

            day = int(time[0:2])
            month = int(time[3:5])
            year = int(time[6:10])

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
            abort(400, "Page number not an integer")

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
            return combined_filtered
        else:
            return combined_filtered[page_start:page_end]

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


