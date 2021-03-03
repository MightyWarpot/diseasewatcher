from flask import Flask
from outbreak_location import location
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@APP.route('/disease/location', methods=['GET'])
def diseaselocation():



if __name__ == "__main__":
    app.run(port=0)
