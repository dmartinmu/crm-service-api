from flask import Blueprint, Response, request
import ujson
from flask_jwt_extended import jwt_required
from cerberus import Validator

from daos import CustomerDAO, CustomerNotFound
from controllers import CustomerController
from utils.exceptions import ResourceNotFoundException, CerberusException

customer_view = Blueprint('customer_view_v1', __name__)


@customer_view.route('/customers/', methods=['GET'])
@jwt_required()
def list_customers():
    data = CustomerDAO().read_all()

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@customer_view.route('/customers/<int:customer_id>/', methods=['GET'])
@jwt_required()
def get_customer(customer_id):
    try:
        data = CustomerDAO().read_one(customer_id)
    except CustomerNotFound:
        exception = ResourceNotFoundException("Customer {} not found".format(customer_id))
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@customer_view.route('/customers/', methods=['POST'])
@jwt_required()
def create_customer():
    # Inputs validation
    v = Validator({
        'name': {'type': 'string', 'required': True},
        'surname': {'type': 'string', 'required': True},
        'id': {'type': 'string', 'required': True},
        'creator_user_id': {'type': 'string', 'required': True},
        'editor_user_id': {'type': 'string', 'required': True}})
    if not v.validate(request.form.to_dict()):
        exception = CerberusException(v)
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )
    
    customer = request.form.to_dict()
    photo_url = None
    if 'photo_file' in request.files:
        photo_file = request.files['photo_file']
        customer_controller = CustomerController()
        photo_url = customer_controller.save_photo(photo_file)
        customer['photo_url'] = photo_url
    data = CustomerDAO().create(customer)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@customer_view.route('/customers/<int:customer_id>/', methods=['PUT'])
@jwt_required()
def update_customer(customer_id):
    # Inputs validation
    v = Validator({
        'name': {'type': 'string', 'required': True},
        'surname': {'type': 'string', 'required': True},
        'id': {'type': 'string', 'required': True},
        'creator_user_id': {'type': 'string', 'required': True},
        'editor_user_id': {'type': 'string', 'required': True}})
    if not v.validate(request.form.to_dict()):
        exception = CerberusException(v)
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )
    
    customer = request.form.to_dict()
    photo_url = None
    if 'photo_file' in request.files:
        photo_file = request.files['photo_file']
        customer_controller = CustomerController()
        photo_url = customer_controller.save_photo(photo_file)
        customer['photo_url'] = photo_url
    try:
        data = CustomerDAO().update(customer_id, customer)
    except CustomerNotFound:
        exception = ResourceNotFoundException("Customer {} not found".format(customer_id))
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )

    return Response(ujson.dumps(data), status=200, mimetype='application/json')


@customer_view.route('/customers/<int:customer_id>/', methods=['DELETE'])
@jwt_required()
def delete_customer(customer_id):
    try:
        CustomerDAO().delete(customer_id)
    except CustomerNotFound:
        exception = ResourceNotFoundException("Customer {} not found".format(customer_id))
        return Response(
            response=ujson.dumps(exception.to_dict()),
            status=exception.status_code,
            mimetype='application/json'
        )
    
    return Response(status=200)
