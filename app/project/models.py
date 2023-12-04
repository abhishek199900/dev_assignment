from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from sqlalchemy import CheckConstraint
from project import db


class User(db.Model, UserMixin):
    """
    Represents a user in the application.

    Attributes:
    - id (int): The unique identifier for the user.
    - username (str): The unique username for the user.
    - email (str): The email address of the user.
    - gender (str): The gender of the user (Male, Female, Others).
    - registration_date (date): The date of user registration.
    - age (int): The age of the user.
    - city (str): The city where the user resides.
    - birthday (date): The birthday of the user.
    - phone_no (str): The phone number of the user.
    - primary_address (str): The primary address of the user.
    - role (str): The role of the user (user, PM, RM, FrontendDeveloper, admin).

    Methods:
    - has_role(self, role): Checks if the user has a specific role.

    Constraints:
    - CheckConstraint(gender.in_(['Male', 'Female', 'Others']), name='check_gender'): Ensures gender is valid.
    - CheckConstraint(role.in_(['user', 'PM', 'RM', 'FrontendDeveloper', 'admin']), name='check_role'): Ensures role is valid.
    """

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(10), nullable=False, server_default='Male')
    registration_date = db.Column(db.Date)
    age = db.Column(db.Integer)
    city = db.Column(db.String(50))
    birthday = db.Column(db.Date)
    phone_no = db.Column(db.String(15))
    primary_address = db.Column(db.Text)

    role = db.Column(db.String(50), default='user')



    __table_args__ = (
        CheckConstraint(gender.in_(['Male', 'Female', "Others"]), name='check_gender'),
        CheckConstraint(role.in_(['user', 'PM', "RM", "FrontendDeveloper", 'admin']), name='check_role'),
    )

    def has_admin_role(self):
        return 'admin' in self.roles.split(',')

    def __repr__(self):
        return f'<User {self.username}>'


class Inventory(db.Model):
    """
    Represents a product in the inventory.

    Attributes:
    - id (int): The unique identifier for the product.
    - product_id (str): The unique product identifier.
    - product_name (str): The name of the product.
    - warehouse (str): The warehouse where the product is stored.
    - seller_id (str): The identifier of the seller.

    Methods:
    - __repr__(): String representation of the Inventory object.

    Returns:
    - str: A string representation of the Inventory.
    """
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), unique=True, nullable=False)
    product_name = db.Column(db.String(100), nullable=False)
    warehouse = db.Column(db.String(50))
    seller_id = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Product {self.product_name}>'


class CustomerActivity(db.Model):
    """
    Represents customer activity.

    Attributes:
    - id (int): The unique identifier for the activity.
    - timestamp (datetime): The timestamp of the activity.
    - uid (int): The user ID associated with the activity.
    - product_id (str): The identifier of the product.
    - add_to_cart (bool): Indicates whether the product was added to the cart.
    - order_placed (bool): Indicates whether an order was placed.

    Methods:
    - __repr__(): String representation of the CustomerActivity object.

    Returns:
    - str: A string representation of the CustomerActivity.
    """
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    product_id = db.Column(db.String(50), nullable=False)
    add_to_cart = db.Column(db.Boolean, default=False)
    order_placed = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<CustomerActivity {self.id}>'


class Purchase(db.Model):
    """
    Represents a purchase record.

    Attributes:
    - id (int): The unique identifier for the purchase.
    - inventory_id (int): The ID of the associated inventory item.
    - quantity (int): The quantity of items purchased.

    Methods:
    - __repr__(): String representation of the Purchase object.

    Returns:
    - str: A string representation of the Purchase.
    """
    id = db.Column(db.Integer, primary_key=True)
    inventory_id = db.Column(db.Integer, db.ForeignKey('inventory.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'<Purchase {self.quantity} items>'



