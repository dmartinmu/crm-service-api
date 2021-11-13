from app.config import db, ma

class User(db.Model):
    """ Object to modelize database user information. """

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50))
    admin = db.Column(db.Boolean)

class UserSchema(ma.SQLAlchemyAutoSchema):
    """ Object to serialize user information. """
    class Meta:
        model = User
        load_instance = True
        sqla_session = db.session 
