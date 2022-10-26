
from flask import Flask
from app.views.user import auth
app = Flask(__name__)

'''registering the routes to blueprints'''
app.register_blueprint(auth)




