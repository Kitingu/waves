from flask import request, jsonify, Blueprint
import json
from marshmallow import ValidationError

from operator import itemgetter
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User as UserModel
from app.utils.validator import UserSchema, LoginSchema

auth = Blueprint('auth', __name__)


@auth.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@auth.route("/signup", methods=['POST'])
def signup():
    user = request.get_json()
    try:
        UserSchema().load(user)
        username = user['username']
        password = user['password']
        email = user['email']
        hashed_password = generate_password_hash(password)
        newUser = UserModel(username, email, hashed_password)
        newUser.create_user()
        print(newUser.get_users())
        return jsonify({"Message": "User registered successfully"}), 201
    except ValidationError as error:
        print('????????', error)
        return jsonify({"Message": error.messages}), 400


@auth.route("/login", methods=['POST'])
def login():
    login_details = request.get_json()
    try:
        LoginSchema().load(login_details)
        username = login_details['username']
        password = login_details['password']
        user = UserModel.get_user('username', username)
        if user:
            is_login = check_password_hash(user['password'], password)
            return jsonify({"Message": "logged in"}), 200
        return jsonify({"Message": "not logged in"}), 200

    except ValidationError as err:
        return jsonify({"Message": err.messages}), 400


@auth.route('/users', methods=['GET'])
def get_users():  # put application's code here
    users = UserModel.get_users()
    return jsonify({

    })
