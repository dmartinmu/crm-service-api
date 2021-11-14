import pytest
import requests


@pytest.fixture
def host():
    url = 'http://127.0.0.1:8000'
    return url


@pytest.fixture
def token_admin_headers(host):
    data = {
        "email": "admin@theagilemonkeys.com",
        "password": "admin1234"
    }
    response = requests.post(host +'/v1/users/login/', data=data)
    token = 'JWT {}'.format(response.json())
    headers = {
        'Authorization': token
    }
    return headers


@pytest.fixture
def token_user_headers(host):
    data = {
        "email": "user@theagilemonkeys.com",
        "password": "user5678"
    }
    response = requests.post(host +'/v1/users/login/', data=data)
    token = 'JWT {}'.format(response.json())
    headers = {
        'Authorization': token
    }
    return headers
