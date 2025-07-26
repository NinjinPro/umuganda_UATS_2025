from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_mail import Mail
from itsdangerous import URLSafeTimedSerializer
from flask_login import LoginManager  
from .config import Config_dev, Config_mail, Config_mail_serializer

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
mail = Mail()
login_manager = LoginManager()  
serializer = None

def create_app():
    print("\n Running Server \n")

    # setting value of the serializer
    global serializer
    serializer = URLSafeTimedSerializer(Config_mail_serializer.SECRET_KEY)

    # flask app creation
    app = Flask(__name__)

    # confuguring the environment variables
    app.config.from_object(Config_dev)
    app.config.from_object(Config_mail)

    # Extensions
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    mail.init_app(app)
    CORS(app)
    
    # Initializing LoginManager with app
    login_manager.init_app(app)
    login_manager.login_view = 'users.login' 

    # Importing models for migration
    from app import models

    # callback for flask-login
    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.get(int(user_id))

    # Registering routing Blueprints
    from .routes import register_routes
    register_routes(app)

    return app
