import json
from marshmallow import ValidationError
from flask import Flask
from operator import itemgetter
import bcrypt
from app.models.user import User as UserModel
from app.utils.validator import UserSchema
from flask import request, jsonify, Blueprint
app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/signup", methods=['POST'])
def userController():
    user = request.get_json()
    print('****',user)
    try:
        error = UserSchema().load(user)
        username = user['username']
        password = user['password']
        email = user['email']
        # username,email,password = itemgetter('username','email','password')(json.dumps(user))
        encodedpassword = password.encode('utf-8')
        hashed_password = bcrypt.hashpw(encodedpassword, bcrypt.gensalt(10))
        newUser = UserModel(username, email, hashed_password)
        newUser.create_user()
        print(newUser.get_users())
        return jsonify({"Message":    newUser.get_user(username)
        }), 200
    except ValidationError as error:
        print('????????',error)
        return jsonify({"Message": error.messages}), 400


