from app.config import db, ma


class Customer(db.Model):
    """ Object to modelize database customer information. """

    __tablename__ = 'customers'
    customer_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    surname = db.Column(db.String(50))
    id = db.Column(db.String(50))
    photo_url = db.Column(db.String(50))
    creator_user_id = db.Column(db.Integer)
    editor_user_id = db.Column(db.Integer)

class CustomerSchema(ma.SQLAlchemyAutoSchema):
    """ Object to serialize customer information. """
    class Meta:
        model = Customer
        load_instance = True
        sqla_session = db.session 
