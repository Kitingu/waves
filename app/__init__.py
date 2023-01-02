from flask import Flask
from flask_cors import CORS

from config.config import Config
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
load_dotenv()

config_name = os.getenv("FLASK_ENV")
db_uri = os.getenv('DATABASE_URI')
if(config_name == "testing"):
    db_uri = os.getenv('TESTDB_URI')
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__,instance_relative_config=True)
    cors = CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_object(Config)
    db.init_app(app)

    # prevent circular imports by importing here
    from .models.user import User
    from .models.wave import Wave
    from app.views.user import auth
    from app.views.wave import wave

    # create tables if they don't exist yet
    with app.app_context():
        print("creating tables")
        db.create_all()
        db.session.commit()

    jwt = JWTManager(app)
    app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY

    '''registering the routes to blueprints'''
    app.register_blueprint(auth)
    app.register_blueprint(wave)
    return app
