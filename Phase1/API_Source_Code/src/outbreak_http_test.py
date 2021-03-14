import json
import sys
import requests


def test_outbreak_location_http(url):
    outbreak_param = {
        "location": 'China',
        "diease": '',
        "time": '',
        "region": '',
        "page": ''
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200


def test_outbreak_disease_http(url):
    outbreak_param = {
        "location": '',
        "diease": 'COVID-19',
        "time": '',
        "region": '',
        "page": ''
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200


def test_outbreak_region_http(url):
    outbreak_param = {
        "location": '',
        "diease": '',
        "time": '',
        "region": 'Asia',
        "page": ''
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200


def test_outbreak_pagination_http(url):
    outbreak_param = {
        "location": '',
        "diease": '',
        "time": '',
        "region": '',
        "page": '1'
    }
    print(url)
    resp = requests.get(f"{url}outbreak/", params=outbreak_param)
    print(resp)
    print(resp.json())
    assert resp.status_code == 200
