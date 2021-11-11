from flask import Flask, Response, request, send_from_directory


# API
app = Flask(__name__)

# v1
from api.v1.user_view import user_view as user_view_v1
from api.v1.customer_view import customer_view as customer_view_v1

app.register_blueprint(user_view_v1, url_prefix='/v1')
app.register_blueprint(customer_view_v1, url_prefix='/v1')
