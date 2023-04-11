from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.config["SECRET_KEY"] = "1234"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///vanibabu.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://jinposgres:123456@localhost:5432/vaniflask"
# app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://payal:123456@localhost:5432/payalflask"


db = SQLAlchemy(app)
becrypt = Bcrypt(app)
login_manager = LoginManager(app)
from fom_login.model import User
from fom_login import route

with app.app_context():
    db.create_all()