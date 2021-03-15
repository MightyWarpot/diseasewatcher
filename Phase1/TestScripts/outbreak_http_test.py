import json
import sys
import requests
import pytest
from time import sleep
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

    not_found = True

    i = 0
    while i < 30 and not_found:
        try:
            resp = requests.get(f"{url}outbreak/", params=outbreak_param)
            print(resp)
            print(resp.json())
            assert resp.status_code == 200
            not_found = False
            return
        except ConnectionError:
            sleep(1)
            i += 1




def test_outbreak_disease_http(url):
    outbreak_param = {
        "location": '',
        "disease": 'COVID-19',
        "start date": '',
        "end date": '',
        "region": '',
        "results": ''
    }
    not_found = True

    i = 0
    while i < 30 and not_found:
        try:
            resp = requests.get(f"{url}outbreak/", params=outbreak_param)
            print(resp)
            print(resp.json())
            assert resp.status_code == 200
            not_found = False
            return
        except ConnectionError:
            sleep(1)
            i += 1




def test_outbreak_region_http(url):
    outbreak_param = {
        "location": '',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": 'Asia',
        "results": ''
    }
    not_found = True

    i = 0
    while i < 30 and not_found:
        try:
            resp = requests.get(f"{url}outbreak/", params=outbreak_param)
            print(resp)
            print(resp.json())
            assert resp.status_code == 200
            not_found = False
            return
        except ConnectionError:
            sleep(1)
            i += 1


def test_outbreak_pagination_http(url):
    outbreak_param = {
        "location": 'China',
        "disease": '',
        "start date": '',
        "end date": '',
        "region": '',
        "results": '1'
    }
    not_found = True

    i = 0
    while i < 30 and not_found:
        try:
            resp = requests.get(f"{url}outbreak/", params=outbreak_param)
            print(resp)
            print(resp.json())
            assert resp.status_code == 200
            not_found = False
            return
        except ConnectionError:
            sleep(1)
            i += 1


def test_outbreak_all_http(url):
    outbreak_param = {
        "location": 'China',
        "disease": 'COVID-19',
        "start date": '',
        "end date": '',
        "region": '',
        "results": ''
    }
    not_found = True

    i = 0
    while i < 30 and not_found:
        try:
            resp = requests.get(f"{url}outbreak/", params=outbreak_param)
            print(resp)
            print(resp.json())
            assert resp.status_code == 200
            not_found = False
            return
        except ConnectionError:
            sleep(1)
            i += 1
