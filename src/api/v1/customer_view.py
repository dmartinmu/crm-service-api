from flask import Blueprint, Response, request, g
import ujson

from daos import CustomerDAO
from controllers import CustomerController

customer_view = Blueprint('customer_view_v1', __name__)


@customer_view.route('/customers/', methods=['GET'])
def list_customers():
    data = CustomerDAO().read_all()

    return Response(ujson.dumps(data), status=200, mimetype='application/json')

@customer_view.route('/customers/<int:customer_id>/', methods=['GET'])
def get_customer(customer_id):
    data = CustomerDAO().read_one(customer_id)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')

@customer_view.route('/customers/', methods=['POST'])
def create_customer():
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
def update_customer(customer_id):
    customer = request.form.to_dict()
    photo_url = None
    if 'photo_file' in request.files:
        photo_file = request.files['photo_file']
        customer_controller = CustomerController()
        photo_url = customer_controller.save_photo(photo_file)
        customer['photo_url'] = photo_url
    data = CustomerDAO().update(customer_id, customer)

    return Response(ujson.dumps(data), status=200, mimetype='application/json')

@customer_view.route('/customers/<int:customer_id>/', methods=['DELETE'])
def delete_customer(customer_id):
    result = CustomerDAO().delete(customer_id)
    if result:
        return Response(status=200)
