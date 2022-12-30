from flask import Flask
from flask_cors import CORS

from config.config import Config
from flask_jwt_extended import JWTManager
import os
from dotenv import load_dotenv
from flask_sqlalchemy import SQLAlchemy




load_dotenv()
db_uri = os.getenv('DB_URL')
print("db_uri", db_uri)


app = Flask(__name__)
cors = CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from .models.user import User
from .models.wave import Wave
from app.views.user import auth
from app.views.wave import wave

with app.app_context():
    print("creating tables")
    db.create_all()
    db.session.commit()

jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY

'''registering the routes to blueprints'''
app.register_blueprint(auth)
app.register_blueprint(wave)
