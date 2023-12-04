from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restful import Api
from flask_login import LoginManager
from flask_principal import Principal, Permission, RoleNeed


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'


db = SQLAlchemy(app)
principal = Principal(app)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'
admin_permission = Permission(RoleNeed('admin'))

migrate = Migrate(app, db)


from project import routes