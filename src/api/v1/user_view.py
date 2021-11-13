from flask import Blueprint, Response, request, g
import ujson

from daos import UserDAO

user_view = Blueprint('user_view_v1', __name__)


@user_view.route('/users/', methods=['GET'])
def list_users():
    data = UserDAO().read_all()

    return Response(ujson.dumps(data), status=200, mimetype='application/json')

@user_view.route('/users/<int:user_id>/', methods=['GET'])
def get_user(user_id):
    data = UserDAO().read_one(user_id)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')

@user_view.route('/users/', methods=['POST'])
def create_user():
    user = request.form.to_dict()
    data = UserDAO().create(user)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')

@user_view.route('/users/<int:user_id>/', methods=['PUT'])
def update_user(user_id):
    user = request.form.to_dict()
    data = UserDAO().update(user_id, user)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')

@user_view.route('/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    result = UserDAO().delete(user_id)
    if result:
        return Response(status=200)
