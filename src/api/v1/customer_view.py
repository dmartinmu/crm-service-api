from flask import Blueprint, Response, request, g
import ujson

customer_view = Blueprint('customer_view_v1', __name__)


@customer_view.route('/customers/', methods=['GET'])
def list_customers():
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')

@customer_view.route('/customers/<int:customer_id>/', methods=['GET'])
def get_customer(customer_id):
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')

@customer_view.route('/customers/', methods=['POST'])
def create_customer():
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')

@customer_view.route('/customers/<int:customer_id>/', methods=['PUT'])
def update_customer(customer_id):
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')

@customer_view.route('/customers/<int:customer_id>/', methods=['DELETE'])
def delete_customer(customer_id):
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')
