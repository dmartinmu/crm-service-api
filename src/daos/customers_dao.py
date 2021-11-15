from models import Customer, CustomerSchema
from app.config import db

class CustomerDAO:
    """ Object to perform database operations over Customer entity."""

    def read_all(self):
        """ Read all existing customers from database.
        
        Returns
        -------
        list
            A list of dictionaries filled with customers' information.
        """
        customers = Customer.query.all()

        customer_schema = CustomerSchema(many=True)
        data = customer_schema.dump(customers)
        return data

    def read_one(self, customer_id):
        """ Read one customer information from database.
        
        Parameters
        ----------
        customer_id: int
            Existing customer database id.
            
        Returns
        -------
        dict:
            Customer Information. None if non existing customer.
        """
        customer = Customer.query.filter(Customer.customer_id == customer_id).one_or_none()

        if not customer:
            raise CustomerNotFound()

        customer_schema = CustomerSchema()
        data = customer_schema.dump(customer)
        return data

    def create(self, customer):
        """ Create a new customer in database. 
        
        Parameters
        ----------
        customer: dict
            New customer information.
        
        Returns
        -------
        dict:
            Created customer information.
        """
        schema = CustomerSchema()
        new_customer = schema.load(customer, session=db.session)

        db.session.add(new_customer)
        db.session.commit()

        data = schema.dump(new_customer)
        
        return data

    def update(self, customer_id, customer):
        """ Update an existing customer in database.
        
        Parameters
        ----------
        customer_id: int
            Database customer id.
        customer: dict
            Customer information to update.
            
        Returns
        -------
        dict:
            Updated customer information.
        """
        existing_customer = Customer.query.filter(Customer.customer_id == customer_id).one_or_none()

        if not existing_customer:
            raise CustomerNotFound()

        schema = CustomerSchema()
        update = schema.load(customer, session=db.session)

        update.customer_id = existing_customer.customer_id
        update.creator_user_id = existing_customer.creator_user_id
        if update.photo_url is None:
            update.photo_url = existing_customer.photo_url

        db.session.merge(update)
        db.session.commit()

        data = schema.dump(update)

        return data

    def delete(self, customer_id):
        """ Delete an existing user in database.
        
        Parameters
        ----------
        customer_id: int
            Database customer id.
            
        Returns
        -------
        boolean:
            True if customer was deleted.
        """
        customer = Customer.query.filter(Customer.customer_id == customer_id).one_or_none()

        if not customer:
            raise CustomerNotFound()

        db.session.delete(customer)
        db.session.commit()
            
        return True

    def generate_photo_url(self, customer_id):
        """ Generates photo URL for a customer.
        
        Parameters
        ----------
        customer_id: int
            Database customer id.
            
        Returns
        -------
        string:
            Photo URL.
        """
        return 'http://localhost:8000/v1/customers/{}/photo/'.format(customer_id)


class CustomerNotFound(Exception):
    """ Custom exception for customer not found. """
    pass

class CustomerPhotoNotFound(Exception):
    """ Custom exception for customer photo not found. """
    pass
