from flask import request, jsonify, Blueprint
import json
from marshmallow import ValidationError
from config.config import Config
import jwt, datetime
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User as UserModel
from app.utils.validator import UserSchema, LoginSchema
from app.utils.auth import token_required

auth = Blueprint('auth', __name__)


@auth.route('/')
def hello_world():  # put application's code here
    return 'Hello World!', 200


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
        return jsonify({"Message": "User registered successfully"}), 201
    except ValidationError as error:
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
            if check_password_hash(user['password'], password):
                access_token = jwt.encode(
                    {"email": user['email']},key=Config.SECRET_KEY, algorithm='HS256')
                return jsonify({"access_token": access_token}), 200
            return jsonify({"Message": "invalid login details"}), 400
        return jsonify({"Message": "invalid login details, try again"}), 400

    except ValidationError as err:
        return jsonify({"Message": err.messages}), 400


@auth.route('/users', methods=['GET'])
@token_required
def get_users():  # put application's code here
    users = UserModel.get_users()
    return jsonify({

    })
