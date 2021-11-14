from flask import Blueprint, Response, request, g
import ujson
from flask_jwt_extended import jwt_required

from daos import UserDAO
from controllers import UserController

user_view = Blueprint('user_view_v1', __name__)


@user_view.route("/users/login/", methods=["POST"])
def login():
    user_data = request.form.to_dict()
    email = user_data.get("email", None)
    password = user_data.get("password", None)
    access_token = UserController().authenticate(email, password)

    return Response(ujson.dumps(access_token), status=200, mimetype='application/json')


@user_view.route('/users/', methods=['GET'])
@jwt_required()
def list_users():
    data = UserDAO().read_all()

    return Response(ujson.dumps(data), status=200, mimetype='application/json')
    

@user_view.route('/users/<int:user_id>/', methods=['GET'])
@jwt_required()
def get_user(user_id):
    data = UserDAO().read_one(user_id)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@user_view.route('/users/', methods=['POST'])
@jwt_required()
def create_user():
    user = request.form.to_dict()
    data = UserDAO().create(user)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@user_view.route('/users/<int:user_id>/', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    user = request.form.to_dict()
    data = UserDAO().update(user_id, user)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@user_view.route('/users/<int:user_id>/', methods=['DELETE'])
@jwt_required()
def delete_user(user_id):
    result = UserDAO().delete(user_id)
    if result:
        return Response(status=200)
