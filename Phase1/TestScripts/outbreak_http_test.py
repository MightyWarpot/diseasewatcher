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
        "results": ''
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
        "results": ''
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
        "results": ''
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
        "results": '1'
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
        "results": ''
    }
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    assert resp.status_code == 200
    articles = resp.json()
    x = datetime.strptime(articles[0]['date'].strip(), '%B %d, %Y')
    startdtime = datetime(2020, 4, 20)
    assert  startdtime <=x 
def test_outbreak_all_http(url):
    outbreak_param = {
        "location": 'China',
        "disease": 'COVID-19',
        "start date": '',
        "end date": '',
        "region": '',
        "results": ''
    }
   
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200
    
        
def test_outbreak_400date_http(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": 'INVALIDDATE',
        "end date": 'INVALIDDATE',
        "region": '',
        "results": ''
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
        "results": ''
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
        "results": '99999999999999999'
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
        "results": '0'
    }
    resp = requests.get(f"{url}outbreak/doesntexist", params=outbreak_param)

    assert resp.status_code == 404
