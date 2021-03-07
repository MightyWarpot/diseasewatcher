from flask import Flask, request
from flask_restplus import Api

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

# sadasd.com/outbreak/?location=China,date=20122020,disease=covid
@api.route('/outbreak/')
class endpoint(Resource):   
    def get(self):
        location = request.args.get('location')
        dtime = request.args.get('date')
        disease = request.args.get('disease')
        res = location_filter(location)
        return dumps(res)

if __name__ == "__main__":
    app.run(port=0, debug=True)
