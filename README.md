# Flask User Management and API

This Flask application serves as an example of user management with Flask-Login, Flask-Principal, and exposes an API endpoint for retrieving the most purchased items.

## Setup and Dependencies

1. **Dependencies:**

   Install the required dependencies by running the following command:

   ```bash
   pip install Flask Flask-SQLAlchemy Flask-Login Flask-Principal Flask-RESTful




1. **Database Setup:**

    Ensure you have a database set up. The application uses SQLAlchemy, so configure the database URI in the project module.

3. **Run the Application:**

    Execute the following command to run the Flask application:

    ```bash
    python run.py


## Application Structure
    * run.py: Entry point for the application.
    * project:
        * models.py: Defines SQLAlchemy models for User, Inventory,  CustomerActivity, and Purchase.
        * views.py: Defines Flask routes, user authentication, and API endpoints.
        * init.py: Initializes Flask app, database, and Flask-Principal.
        * templates: (not provided in the code) Place your HTML templates here if needed.

## Models

# User

    * Represents a user in the application.
    * Attributes:
    * id (int)
    * username (str)
    * email (str)
    * gender (str)
    * registration_date (date)
    * age (int)
    * city (str)
    * birthday (date)
    * phone_no (str)
    * primary_address (str)
    * role (str)

# Methods:
    * has_role(self, role)

# Constraints:
    * CheckConstraint(gender.in_(['Male', 'Female', 'Others']), name='check_gender')
    * CheckConstraint(role.in_(['user', 'PM', 'RM', 'FrontendDeveloper', 'admin']), name='check_role')

# Inventory
    * Represents a product in the inventory.
    * Attributes:
        * id (int)
        * product_id (str)
        * product_name (str)
        * warehouse (str)
        * seller_id (str)

# CustomerActivity
    *Represents customer activity.
    *Attributes:
        *id (int)
        *timestamp (datetime)
        *uid (int)
        *product_id (str)
        *add_to_cart (bool)
        *order_placed (bool)

# Purchase
    *Represents a purchase record.
    * Attributes:
        * id (int)
        * inventory_id (int)
        * quantity (int)
        * Additional Features
        * User authentication using Flask-Login.
        * Role-based access control using Flask-Principal.
        * API endpoint /most_purchased_items to retrieve the top 10 most purchased items.
