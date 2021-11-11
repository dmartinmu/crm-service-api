from flask import Blueprint, Response, request, g
import ujson

user_view = Blueprint('user_view_v1', __name__)


@user_view.route('/users/', methods=['GET'])
def list_users():
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')

@user_view.route('/users/', methods=['POST'])
def create_user():
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')

@user_view.route('/users/<int:user_id>/', methods=['PUT'])
def update_user(user_id):
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')

@user_view.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(customer_id):
    result = {"result": "ok"}
    return Response(ujson.dumps(result), status=200, mimetype='application/json')
