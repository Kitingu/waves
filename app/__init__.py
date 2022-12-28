from flask import Flask
from flask_cors import CORS
from app.views.user import auth
from app.views.wave import wave
from config.config import Config
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy
from .models.user import User

load_dotenv()
db_uri = "mssql+pyodbc://" + os.getenv("DB_USER") + ":" + os.getenv("DB_PASSWORD") + "@" + os.getenv(
    "DB_SERVER_NAME") + "/" + os.getenv("DB_NAME") + "?driver=" + os.getenv("DB_DRIVER_NAME")
db = SQLAlchemy()

app = Flask(__name__)
cors = CORS(app)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db.init_app(app)

with app.app_context():
    print("creating tables")
    db.create_all()
    db.session.commit()

jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY

'''registering the routes to blueprints'''
app.register_blueprint(auth)
app.register_blueprint(wave)
