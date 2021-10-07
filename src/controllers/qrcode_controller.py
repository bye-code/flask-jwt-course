from flask import request, make_response, jsonify
from flask.views import MethodView
from src.services.qrcode_service import QrcodeService

class QrcodeController(MethodView):

    def get(self):
        if request.is_json:
            data = request.args.get("data", "")
            return QrcodeService.create_qrcode(data)
        response = make_response(jsonify({
            "response": {
                "statusCode": 400,
                "message": "Invalid request",
                "data": []
            }
        }), 400)
        return response

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass
