import json
import sys
import requests
import pytest

url = 'http://127.0.0.1:8000/'

def test_outbreak_location_http():
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
    print(resp)
    print(resp.json())
    assert resp.status_code == 200


def test_outbreak_disease_http(url):
    outbreak_param = {
        "location": '',
        "disease": 'COVID-19',
        "start date": '',
        "end date": '',
        "region": '',
        "results": ''
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200


def test_outbreak_region_http(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": 'Asia',
        "results": ''
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200


def test_outbreak_pagination_http(url):
    outbreak_param = {
        "location": 'China',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '1'
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200


def test_outbreak_all_http(url):
    outbreak_param = {
        "location": 'Vietnam',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": ''
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200
