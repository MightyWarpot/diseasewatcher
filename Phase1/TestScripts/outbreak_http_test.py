import json
import sys
import requests
import pytest
from time import sleep
from datetime import *
from requests.exceptions import ConnectionError

def test_outbreak_location_http(url):
    print(url)
    outbreak_param = {
        "location": 'China',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '',
        "start_index": ''
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    assert resp.status_code == 200
    articles = resp.json()
    assert articles[0]['location'] == 'China'
    assert articles[1]['location'] == 'China'
    assert articles[2]['location'] == 'China'
    
      




def test_outbreak_disease_http(url):
    outbreak_param = {
        "location": '',
        "disease": 'COVID-19',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '',
        "start_index": ''
    }
    
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    assert resp.status_code == 200
    articles = resp.json()
    assert articles[0]['disease'] == 'COVID-19'
        




def test_outbreak_region_http(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": 'Asia',
        "results": '',
        "start_index": ''
    }
   
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    articles = resp.json()
    assert resp.status_code == 200
    assert articles[0]['region'] == 'Asia'
           


def test_outbreak_pagination_http(url):
    outbreak_param = {
        "location": 'China',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '1',
        "start_index": ''
    }
    
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    articles = resp.json()
    assert resp.status_code == 200
    assert len(articles) == 1
           
def test_outbreak_date(url):
    outbreak_param = {
        "location": 'China',
        "disease": '',
        "start date": '20/04/2020',
        "end date": '20/04/2021',
        "region": '',
        "results": '',
        "start_index": ''
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    assert resp.status_code == 200
    articles = resp.json()
    startdtime = datetime(2020, 4, 20)
    endtime = datetime(2021, 4,20)
    for article in articles:
        x = datetime.strptime(article['date'].strip(), '%B %d, %Y')
        
        assert  startdtime <=x and x <= endtime 
def test_outbreak_all_http(url):
    outbreak_param = {
        "location": 'United States',
        "disease": 'mosquito-borne Zika',
        "start date": '10/02/2016',
        "end date": '10/02/2017',
        "region": 'US News',
        "results": '1',
        "start_index": ''
    }
   
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
  
    assert resp.status_code == 200
    articles = resp.json()
    startdtime = datetime(2016, 2, 10)
    endtime = datetime(2017, 2,10)
    for article in articles:
        x = datetime.strptime(article['date'].strip(), '%B %d, %Y')
        
        assert  startdtime <=x and x <= endtime and article['location'] == 'United States'
        assert article['disease'] == 'mosquito-borne Zika' and article['region'] == 'US News'
    
        
def test_outbreak_400date_http(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": 'INVALIDDATE',
        "end date": 'INVALIDDATE',
        "region": '',
        "results": '',
        "start_index": ''
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)

    assert resp.status_code == 400


def test_outbreak_400empty_http(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '',
        "start_index": ''
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)

    assert resp.status_code == 400


def test_outbreak_400results_http(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '99999999999999999',
        "start_index": ''
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)

    assert resp.status_code == 400


def test_outbreak_500_http(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '0',
        "start_index": ''
    }
    resp = requests.get(f"{url}outbreak/doesntexist", params=outbreak_param)

    assert resp.status_code == 404


def test_outbreak_pagination_http(url):
    outbreak_param = {
        "location": 'China',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '5',
        "start_index": '5'
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)

    assert resp.status_code == 200


def test_outbreak_pagination_http_nootherinput(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '5',
        "start_index": '5'
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)

    assert resp.status_code == 400


def test_outbreak_pagination_http_nostartindex(url):
    outbreak_param = {
        "location": 'China',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '5',
        "start_index": ''
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)

    assert resp.status_code == 200


def test_outbreak_pagination_http_noresultsinput(url):
    outbreak_param = {
        "location": 'China',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '',
        "start_index": '5'
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)

    assert resp.status_code == 400
