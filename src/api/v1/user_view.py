from flask import Blueprint, Response, request
import ujson
from flask_jwt_extended import jwt_required
from cerberus import Validator

from daos import UserDAO, UserNotFound
from controllers import UserController
from api.v1 import validate_admin
from utils.exceptions import ResourceNotFoundException, CerberusException

user_view = Blueprint('user_view_v1', __name__)


@user_view.route("/users/login/", methods=["POST"])
def login():
    # Inputs validation
    v = Validator({
        'email': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True}})
    if not v.validate(request.form.to_dict()):
        exception = CerberusException(v)
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )
    
    user_data = request.form.to_dict()
    email = user_data.get("email", None)
    password = user_data.get("password", None)
    access_token = UserController().authenticate(email, password)

    return Response(ujson.dumps(access_token), status=200, mimetype='application/json')


@user_view.route('/users/', methods=['GET'])
@jwt_required()
@validate_admin
def list_users():
    data = UserDAO().read_all()

    return Response(ujson.dumps(data), status=200, mimetype='application/json')
    

@user_view.route('/users/<int:user_id>/', methods=['GET'])
@jwt_required()
@validate_admin
def get_user(user_id):
    try:
        data = UserDAO().read_one(user_id)
    except UserNotFound:
        exception = ResourceNotFoundException("User {} not found".format(user_id))
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@user_view.route('/users/', methods=['POST'])
@jwt_required()
@validate_admin
def create_user():
    # Inputs validation
    v = Validator({
        'email': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True},
        'admin': {'type': 'string', 'required': True}})
    if not v.validate(request.form.to_dict()):
        exception = CerberusException(v)
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )
    
    user = request.form.to_dict()
    user['password_hash'] = UserController().generate_password_hash(user['password'])
    del(user['password'])
    data = UserDAO().create(user)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@user_view.route('/users/<int:user_id>/', methods=['PUT'])
@jwt_required()
@validate_admin
def update_user(user_id):
    # Inputs validation
    v = Validator({
        'email': {'type': 'string', 'required': True},
        'password': {'type': 'string', 'required': True},
        'admin': {'type': 'string', 'required': True}})
    if not v.validate(request.form.to_dict()):
        exception = CerberusException(v)
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )
    
    user = request.form.to_dict()
    user['password_hash'] = UserController().generate_password_hash(user['password'])
    del(user['password'])
    try:
        data = UserDAO().update(user_id, user)
    except UserNotFound:
        exception = ResourceNotFoundException("User {} not found".format(user_id))
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@user_view.route('/users/<int:user_id>/', methods=['DELETE'])
@jwt_required()
@validate_admin
def delete_user(user_id):
    try:
        UserDAO().delete(user_id)
    except UserNotFound:
        exception = ResourceNotFoundException("User {} not found".format(user_id))
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )
    return Response(status=200)
