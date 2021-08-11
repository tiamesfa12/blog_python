from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from os import path
from flask_login import LoginManager 

db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "helloworld"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post, Comment, Like 

    create_database(app) 

    login_manager = LoginManager()
    login_manager.login_view = "auth.login" # if someone tries to access without an account logged in, redirects them to the login url
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id)) # this uses a session to store an id of a user that logged in 

    return app

def create_database(app):
    if not path.exists("website/" + DB_NAME): # we are checking if the path exists, if it doesnt exist then we create it
        db.create_all(app=app)
        print("Created database!") 