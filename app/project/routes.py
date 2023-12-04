from flask import jsonify
from flask import render_template_string

from project import app
from project import db
from project import login_manager
from project import admin_permission

from flask_login import LoginManager
from flask_login import login_user
from flask_login import login_required
from flask_login import current_user
from flask_login import logout_user

from flask_restful import Resource

from project.models import User
from project.models import Inventory
from project.models import Purchase

from flask_principal import identity_loaded

from sqlalchemy import func


@login_manager.user_loader
def load_user(user_id):
    """
    Load a user from the database by user ID.

    Parameters:
    - user_id (int): The ID of the user to load.

    Returns:
    - User: The User object corresponding to the provided user ID.
    """
    return User.query.get(int(user_id))


@app.route('/')
@login_required
def home():
    """
    Render the home page for an authenticated user.

    Returns:
    - str: A personalized greeting for the logged-in user.
    """
    return f'Hello, {current_user.username}! You are logged in. Your role: {current_user.role}'


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    """
    Connect identity loading to add user roles to Flask-Principal identity.

    Parameters:
    - sender: The sender of the signal.
    - identity: The Flask-Principal identity object.

    Returns:
    - None
    """
    identity.user = current_user
    if hasattr(current_user, 'roles'):
        for role in current_user.roles.split(','):
            identity.provides.add(RoleNeed(role))
        identity.provides.add(UserNeed(current_user.id))


@app.route('/admin')
@admin_permission.require(http_exception=403)
@login_required
def admin():

    """
    Render the admin page for users with admin access.

    Returns:
    - str: A greeting for users with admin access.
    """
    return f'Hello, {current_user.username}! You have admin access.'


@app.route('/login/<username>')
def login(username):
    """
    Log in a user with the provided username.

    Parameters:
    - username (str): The username of the user to log in.

    Returns:
    - str: A greeting message upon successful login or an error message if the user is not found.
    """
    user = User.query.filter_by(username=username).first()
    if user:
        login_user(user)
        return render_template_string(f"<h1> Hello {user.username}</h1>")
    return 'User not found.'


@app.route('/logout')
@login_required
def logout():
    """
    Log out the currently logged-in user.

    Returns:
    - str: A message indicating successful logout.
    """
    logout_user()
    return 'Logged out successfully.'


@app.route('/most_purchased_items', methods=['GET'])
def most_purchased_items():
    """
    Retrieve the most purchased items from the database.

    Returns:
    - jsonify: A JSON response containing the top 10 most purchased items and their total quantities.
    """
    top_items = db.session.query(
        Inventory.product_name,
        func.sum(Purchase.quantity).label('total_quantity')
        ).join(Purchase).group_by(Inventory.product_name).order_by(func.sum(Purchase.quantity).desc()).limit(10).all()

    result = [{'product_name': item.product_name, 'total_quantity': item.total_quantity} for item in top_items]
    return jsonify(result)