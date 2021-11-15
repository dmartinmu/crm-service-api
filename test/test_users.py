import requests
import pytest


def test_login(host):
    route = '/v1/users/login/'
    data = {
        "email": "user@theagilemonkeys.com",
        "password": "user5678"
    }
    response = requests.post(host + route, data=data)

    assert response.status_code == 200


def test_list_users(host, token_admin_headers):
    route = '/v1/users/'
    response = requests.get(host + route, headers=token_admin_headers)

    assert response.status_code == 200
    assert len(response.json()) == 4


def test_list_users_forbidden(host, token_user_headers):
    route = '/v1/users/'
    response = requests.get(host + route, headers=token_user_headers)

    assert response.status_code == 403


def test_list_users_unauthorized(host):
    route = '/v1/users/'
    response = requests.get(host + route)

    assert response.status_code == 401


def test_get_user(host, token_admin_headers):
    route = '/v1/users/1/'
    response = requests.get(host + route, headers=token_admin_headers)
    data = response.json()

    assert response.status_code == 200
    assert data['email'] == 'admin@theagilemonkeys.com'


def test_get_user_not_found(host, token_admin_headers):
    route = '/v1/users/7/'
    response = requests.get(host + route, headers=token_admin_headers)
    data = response.json()

    assert response.status_code == 404


def test_get_user_forbidden(host, token_user_headers):
    route = '/v1/users/1/'
    response = requests.get(host + route, headers=token_user_headers)

    assert response.status_code == 403


def test_get_user_unauthorized(host):
    route = '/v1/users/1/'
    response = requests.get(host + route)

    assert response.status_code == 401


def test_create_user(host, token_admin_headers):
    data = {
        'email': 'user_created@test.com',
        'password': '1234',
        'admin': False
    }
    route = '/v1/users/'
    response = requests.post(host + route, headers=token_admin_headers, data=data)
    data = response.json()

    assert response.status_code == 200

    # Delete created user 
    route = '/v1/users/{}/'.format(data['user_id'])
    response = requests.delete(host + route, headers=token_admin_headers)


def test_create_user_forbidden(host, token_user_headers):
    data = {
        'email': 'user_created@test.com',
        'password': '1234',
        'admin': False
    }
    route = '/v1/users/'
    response = requests.post(host + route, headers=token_user_headers, data=data)

    assert response.status_code == 403
    

def test_create_user_unauthorized(host):
    data = {
        'email': 'user_created@test.com',
        'password': '1234',
        'admin': False
    }
    route = '/v1/users/'
    response = requests.post(host + route, data=data)

    assert response.status_code == 401
    

def test_update_user(host, token_admin_headers):
    data = {
        'email': 'test2@test.com',
        'password': 'pass',
        'admin': False
    }
    route = '/v1/users/4/'
    response = requests.put(host + route, headers=token_admin_headers, data=data)
    data = response.json()

    assert response.status_code == 200


def test_update_user_not_found(host, token_admin_headers):
    data = {
        'email': 'test2@test.com',
        'password': 'pass',
        'admin': False
    }
    route = '/v1/users/7/'
    response = requests.put(host + route, headers=token_admin_headers, data=data)
    data = response.json()

    assert response.status_code == 404


def test_update_user_forbidden(host, token_user_headers):
    data = {
        'email': 'test2@test.com',
        'password': 'pass',
        'admin': False
    }
    route = '/v1/users/4/'
    response = requests.put(host + route, headers=token_user_headers, data=data)

    assert response.status_code == 403


def test_update_user_unauthorized(host):
    data = {
        'email': 'test2@test.com',
        'password': 'pass',
        'admin': False
    }
    route = '/v1/users/4/'
    response = requests.put(host + route, data=data)

    assert response.status_code == 401


def test_delete_user(host, token_admin_headers):
    route = '/v1/users/3/'
    response = requests.delete(host + route, headers=token_admin_headers)

    assert response.status_code == 200


def test_delete_user_not_found(host, token_admin_headers):
    route = '/v1/users/7/'
    response = requests.delete(host + route, headers=token_admin_headers)

    assert response.status_code == 404


def test_delete_user_forbidden(host, token_user_headers):
    route = '/v1/users/3/'
    response = requests.delete(host + route, headers=token_user_headers)

    assert response.status_code == 403


def test_delete_user_unauthorized(host):
    route = '/v1/users/3/'
    response = requests.delete(host + route)

    assert response.status_code == 401
