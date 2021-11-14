from functools import wraps

from flask import g
from flask_jwt_extended import get_jwt_identity


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
            raise Exception 
        return func(*args, **kwargs)
    return func_wrapper
