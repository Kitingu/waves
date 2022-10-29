from functools import wraps
from flask import request, jsonify
from config.config import Config
import jwt


def token_required(f):
    """Checks for authenticated users with valid token in the header"""

    @wraps(f)
    def decorated(*args, **kwargs):
        """ make a token_required decorator"""
        token = None

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({"message": "Please Sign up and Login"}), 401

        try:
            jwt.decode(token,key= Config.SECRET_KEY,algorithms=["HS256"], )
        except():
            return jsonify({"message": "Please, provide a valid token."}), 401
        return f(*args, **kwargs)

    return decorated
