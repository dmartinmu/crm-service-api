from datetime import timedelta
import json
import os

from flask import Flask, Response, request, send_from_directory
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError
from flask_swagger_ui import get_swaggerui_blueprint
import yaml

yaml.warnings({'YAMLLoadWarning': False})
from yaml import load


# API
app = Flask(__name__)

# JWT Configuration
token_expires = timedelta(seconds=1296000)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = token_expires
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'JWT'
app.config['JWT_SECRET_KEY'] = '$5$36820$7ymGjg/vQApRRYAcGptZICN7ncgkAQx7WltYewC3/I2_CRM'
jwt = JWTManager(app)

# Add Swagger UI blueprint
spec_path = os.path.realpath(os.path.join(os.path.realpath(__file__), '../../specs/openapi_spec.yaml'))
with open(spec_path, 'rt', encoding='utf8') as yml:
    spec = load(yml)
swagger_api = get_swaggerui_blueprint(
    base_url='/v1',
    api_url=spec_path,
    config={'app_name': 'CRM Service API', 'spec': spec},
    oauth_config=None,
    blueprint_name='swagger_api_v1',
)

# v1
from api.v1.user_view import user_view as user_view_v1
from api.v1.customer_view import customer_view as customer_view_v1

app.register_blueprint(user_view_v1, url_prefix='/v1')
app.register_blueprint(customer_view_v1, url_prefix='/v1')
app.register_blueprint(swagger_api, url_prefix='/v1')

# Endpoint to check if API is up and running. 
@app.route('/health/', methods=['GET'])
def health():
    return Response(
        response=json.dumps({'message': 'The API is running'}),
        status=200,
        mimetype='application/json'
    )
