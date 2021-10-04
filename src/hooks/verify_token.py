from os import getenv
from flask import request, make_response, jsonify
from functools import wraps
import jwt

def verify_token(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        token: str = request.headers.get('Authorization', type=str)
        try:
            read_token = jwt.decode(token, getenv('JWT_SECRET_KEY'), algorithms=['HS256'])
            print(read_token)
        except jwt.DecodeError:
            return make_response(jsonify({
                "error": "Token is missing or invalid"
            }), 401)
        except jwt.ExpiredSignatureError:
            return make_response(jsonify({
                "error": "Token is expire"
            }), 401)
        except jwt.InvalidTokenError:
            return make_response(jsonify({
                "error": "Token error"
            }), 401)
        return function(*args, *kwargs)
    return wrapper
