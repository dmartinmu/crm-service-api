from werkzeug.security import check_password_hash, generate_password_hash
from flask_jwt_extended import create_access_token

from daos import UserDAO


class UserController():
    """ Object to perform actions on User information. """

    def authenticate(self, username, password):
        user = UserDAO().read_one_by_email(username)

        if check_password_hash(user['password_hash'], password):
            return create_access_token(identity={
                'email': user['email'],
                'id': user['user_id'],
                'admin': user['admin']})

    def generate_password_hash(self, raw_password):
        return generate_password_hash(raw_password)
