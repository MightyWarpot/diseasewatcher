from flask import Flask, request
from outbreak_location import location_filter
from json import dumps
app = Flask(__name__)


# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


@app.route('/outbreak/search', methods=['GET'])
def outbreaksearch():
    location = request.args.get('location')
    disease = request.args.get('disease')
    res = location_filter(location)

    return dumps(res)


@app.route('/outbreak/location', methods=['GET'])
def outbreaklocation():
    location = request.args.get('location')
    res = location_filter(location)

    return dumps(res)

if __name__ == "__main__":
    app.run(port=0, debug=True)
