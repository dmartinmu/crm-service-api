from datetime import timedelta

from flask import Flask, Response, request, send_from_directory
from flask_jwt_extended import JWTManager
from flask_jwt_extended.exceptions import NoAuthorizationError


# API
app = Flask(__name__)

# JWT Configuration
token_expires = timedelta(seconds=1296000)
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = token_expires
app.config['JWT_HEADER_NAME'] = 'Authorization'
app.config['JWT_HEADER_TYPE'] = 'JWT'
app.config['JWT_SECRET_KEY'] = '$5$36820$7ymGjg/vQApRRYAcGptZICN7ncgkAQx7WltYewC3/I2_CRM'
jwt = JWTManager(app)

# v1
from api.v1.user_view import user_view as user_view_v1
from api.v1.customer_view import customer_view as customer_view_v1

app.register_blueprint(user_view_v1, url_prefix='/v1')
app.register_blueprint(customer_view_v1, url_prefix='/v1')
