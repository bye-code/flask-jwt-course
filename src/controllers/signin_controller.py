from flask import request, make_response, jsonify
from flask.views import MethodView
from src.services.auth_service import AuthService

class SigninController(MethodView):

    def __init__(self) -> None:
        self.auth_service = AuthService()

    def post(self):
        if request.is_json:
            email = request.json['email']
            password = request.json['password']
            return self.auth_service.signin(email, password)
        response = make_response(jsonify({
            "error": "Invalid request, please send me a JSON FORMAT"
        }), 400)
        return response
