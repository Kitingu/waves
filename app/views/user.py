from flask import request, jsonify, Blueprint
from marshmallow import ValidationError
from flask_jwt_extended import create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from app.models.user import User as UserModel
from app.utils.validator import UserSchema, LoginSchema
from flask_jwt_extended import jwt_required
import uuid
from datetime import date

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
        username_exists = UserModel.get_user('username', username)
        email_exists = UserModel.get_user('email', email)
        if username_exists:
            return jsonify({"message": "username already exists"}), 409
        if email_exists:
            return jsonify({"message": "email already exists"}), 409

        hashed_password = generate_password_hash(password)
        newUser = UserModel(username=username, email=email, password=hashed_password, user_id=str(uuid.uuid4()),
                            date_created=date.today().strftime("%d/%m/%Y"), is_admin="False")
        serialized_user = newUser.create_user()
        return jsonify({"Message": "User registered successfully",
                        "user": serialized_user}), 201

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
                access_token = create_access_token(identity=username)
                return jsonify({"access_token": access_token}), 200
            return jsonify({"Message": "invalid login details"}), 400
        return jsonify({"Message": "invalid login details, try again"}), 400

    except ValidationError as err:
        return jsonify({"Message": err.messages}), 400


@auth.route('/users', methods=['GET'])
@jwt_required
def get_users():  # put application's code here
    users = UserModel.get_users()
    return jsonify({
        "message": users
    })
