import requests
import pytest


def test_list_customers(host, token_user_headers):
    route = '/v1/customers/'
    response = requests.get(host + route, headers=token_user_headers)

    assert response.status_code == 200
    assert len(response.json()) == 3


def test_list_customers_unauthorized(host):
    route = '/v1/customers/'
    response = requests.get(host + route)

    assert response.status_code == 401


def test_get_customer(host, token_admin_headers):
    route = '/v1/customers/1/'
    response = requests.get(host + route, headers=token_admin_headers)
    data = response.json()

    assert response.status_code == 200
    assert data['surname'] == 'Neal'


def test_get_customer_not_found(host, token_admin_headers):
    route = '/v1/customers/7/'
    response = requests.get(host + route, headers=token_admin_headers)
    data = response.json()

    assert response.status_code == 404


def test_get_customer_unauthorized(host):
    route = '/v1/customers/1/'
    response = requests.get(host + route)

    assert response.status_code == 401


def test_create_customer(host, token_admin_headers):
    data = {
        'name': 'John',
        'surname': 'Doe',
        'id': '123987A',
        'creator_user_id': '1',
        'editor_user_id': '1'
    }
    route = '/v1/customers/'
    response = requests.post(host + route, headers=token_admin_headers, data=data)
    data = response.json()

    assert response.status_code == 200

    # Delete created customer 
    route = '/v1/customers/{}/'.format(data['customer_id'])
    response = requests.delete(host + route, headers=token_admin_headers)


def test_create_customer_unauthorized(host):
    data = {
        'name': 'John',
        'surname': 'Doe',
        'id': '123987A',
        'creator_user_id': '1',
        'editor_user_id': '1'
    }
    route = '/v1/customers/'
    response = requests.post(host + route, data=data)

    assert response.status_code == 401
    

def test_update_customer(host, token_admin_headers):
    data = {
        'name': 'John',
        'surname': 'Doe',
        'id': '123987A',
        'creator_user_id': '1',
        'editor_user_id': '1'
    }
    route = '/v1/customers/2/'
    response = requests.put(host + route, headers=token_admin_headers, data=data)
    data = response.json()

    assert response.status_code == 200


def test_update_customer_not_found(host, token_admin_headers):
    data = {
        'name': 'John',
        'surname': 'Doe',
        'id': '123987A',
        'creator_user_id': '1',
        'editor_user_id': '1'
    }
    route = '/v1/customers/7/'
    response = requests.put(host + route, headers=token_admin_headers, data=data)
    data = response.json()

    assert response.status_code == 404


def test_update_customer_unauthorized(host):
    data = {
        'name': 'John',
        'surname': 'Doe',
        'id': '123987A',
        'creator_user_id': '1',
        'editor_user_id': '1'
    }
    route = '/v1/customers/4/'
    response = requests.put(host + route, data=data)

    assert response.status_code == 401


def test_delete_customer(host, token_admin_headers):
    route = '/v1/customers/3/'
    response = requests.delete(host + route, headers=token_admin_headers)

    assert response.status_code == 200


def test_delete_customer_not_found(host, token_admin_headers):
    route = '/v1/customers/7/'
    response = requests.delete(host + route, headers=token_admin_headers)

    assert response.status_code == 404


def test_delete_customer_unauthorized(host):
    route = '/v1/customers/3/'
    response = requests.delete(host + route)

    assert response.status_code == 401
