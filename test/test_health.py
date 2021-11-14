import requests


def test_api_running(host):
    route = '/health/'
    r = requests.get(host + route)
    assert r.status_code == 200 
