from functools import wraps
import ujson

from flask import Response
from flask_jwt_extended import get_jwt_identity

from utils.exceptions import APIException


def validate_admin(func):
    """ Check if user making the request has admin role.

    Returns
    -------
    function
    """
    @wraps(func)
    def func_wrapper(*args, **kwargs):
        user = get_jwt_identity()
        admin = user['admin']
        if not admin:
            exception= APIException(403) 
            return Response(
                response=ujson.dumps(exception.to_dict()),
                status=exception.status_code,
                mimetype='application/json'
            )
        return func(*args, **kwargs)
    return func_wrapper
