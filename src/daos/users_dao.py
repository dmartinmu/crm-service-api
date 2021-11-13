from models import User, UserSchema
from app.config import db

class UserDAO:
    """ Object to perform database operations over User entity."""

    def read_all(self):
        """ Read all existing users from database.
        
        Returns
        -------
        list
            A list of dictionaries filled with users' information.
        """
        users = User.query.all()

        user_schema = UserSchema(many=True)
        data = user_schema.dump(users)
        return data

    def read_one(self, user_id):
        """ Read one user information from database.
        
        Parameters
        ----------
        user_id: int
            Existing user database id.
            
        Returns
        -------
        dict:
            User Information. None if non existing user.
        """
        user = User.query.filter(User.user_id == user_id).one_or_none()

        if user is not None:
            user_schema = UserSchema()
            data = user_schema.dump(user)
            return data
        else:
            return None

    def create(self, user):
        """ Create a new user in database. 
        
        Parameters
        ----------
        user: dict
            New user information.
        
        Returns
        -------
        dict:
            Created user information.
        """
        schema = UserSchema()
        new_user = schema.load(user, session=db.session)

        db.session.add(new_user)
        db.session.commit()

        data = schema.dump(new_user)

        return data

    def update(self, user_id, user):
        """ Update an existing user in database.
        
        Parameters
        ----------
        user_id: int
            Database user id.
        user: dict
            User information to update.
            
        Returns
        -------
        dict:
            Updated user information.
        """
        existing_user = User.query.filter(User.user_id == user_id).one_or_none()

        schema = UserSchema()
        update = schema.load(user, session=db.session)
        update.user_id = existing_user.user_id

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update)

        return data

    def delete(self, user_id):
        """ Delete an existing user in database.
        
        Parameters
        ----------
        user_id: int
            Database user id.
            
        Returns
        -------
        boolean:
            True if user was deleted. False otherwise.
        """
        user = User.query.filter(User.user_id == user_id).one_or_none()

        if user is not None:
            db.session.delete(user)
            db.session.commit()
            
        return True
