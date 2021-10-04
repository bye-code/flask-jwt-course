from flask import request, make_response, jsonify
from werkzeug.security import check_password_hash, generate_password_hash
from os import getenv
from src.database import db
from src.models.users_model import User
import jwt, datetime

class AuthService:

    def signin(self, email: str, password: str):
        user = User.query.filter_by(email=email).first()
        if user or user is not None:
            verify_password = check_password_hash(user.password, password)
            if verify_password:
                try:
                    token: str = jwt.encode({
                        "sub": user.uid,
                        "email": user.email,
                        "password": user.password,
                        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                    }, getenv("JWT_SECRET_KEY"), algorithm="HS256")
                    response = make_response(jsonify({
                        "message": f"Success! You're logged in {user.name}",
                        "token": token
                    }), 201)
                    response.headers['Authorization'] = token
                    return response
                except jwt.InvalidKeyError as e:
                    return make_response(jsonify({
                        "error": "Invalid token error"
                    }), 401)
            return make_response(jsonify({
                "error": "Wrong credentials"
            }), 401)
        response = make_response(jsonify({
            "error": "User doesn't exists"
        }), 401)
        return response

    def signup(self, email: str, password: str, name: str, last_name: str):
        user = User.query.filter_by(email=email).first()
        if not user or user is None:
            hash_password = generate_password_hash(password)
            try:
                new_user = User(email, hash_password, name, last_name)
                db.session.add(new_user)
                db.session.commit()
                token: str = jwt.encode({
                    "email": email,
                    "name": name,
                    "last_name": last_name,
                    "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=60)
                }, getenv("JWT_SECRET_KEY"), algorithm="HS256")
                response = make_response(jsonify({
                    "message": "Success! Your account was signup",
                    "token": token
                }), 201)
                response.headers['Authorization'] = token
                return response
            except jwt.InvalidKeyError as e:
                return make_response(jsonify({
                    "error": "Token key error"
                }), 401)
            except Exception as e:
                return make_response(jsonify({
                    "error": "Token error"
                }), 401)
        response = make_response(jsonify({
            "error": "User exists"
        }), 400)
        return response
