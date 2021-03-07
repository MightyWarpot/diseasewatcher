import json
import sys
import requests


def test_outbreak_location_http(url):
    location_param = {
        "location": 'China'
    }
    resp = requests.get(f"{url}outbreak/location", params=location_param)
    assert resp.status_code == 200
    # print(resp)
    # print(resp.json())
