
from flask import Flask
from app.views.user import auth
from app.views.wave import wave
from config.config import Config
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# jwt = JWTManager(app)
# app.config["JWT_SECRET_KEY"] =Config.SECRET_KEY

'''registering the routes to blueprints'''
app.register_blueprint(auth)
app.register_blueprint(wave)




