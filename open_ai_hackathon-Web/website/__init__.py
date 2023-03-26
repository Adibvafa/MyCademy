from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
from os import path
# from flask_login import LoginManager

# db = SQLAlchemy()
# DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'THE CYBER SAVVY NINJAS'

    # for database
    # app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    # db.init_app(app)          # assigning the database to this application

    # defining the schema of this database is done in models.py

    # after defining blueprints, we need to register them here
    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')    # specifies a prefix that we have to put before any of the blueprint paths
    app.register_blueprint(auth, url_prefix='/')

    # check if we've already created a database
    # from .models import User, Note
    # create_database(app)

    # telling flask how we find a user or something like that
    # login_manager = LoginManager()
    # login_manager.login_view = 'auth.login'
    # login_manager.init_app(app)

    # tells flask how we load a user
    # @login_manager.user_loader
    # def load_user(id):
        # return User.query.get(int(id))

    return app

# def create_database(app):
#     with app.app_context():
#         if not path.exists('website/' + DB_NAME):
#             db.create_all()
#             print('Created Database!')