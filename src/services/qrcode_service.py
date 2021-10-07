from flask import request, make_response, jsonify, send_file
from flask_qrcode import QRcode, Image
from os import getenv
import qrcode

class QrcodeService:

    qrc = qrcode.QRCode(version=1, error_correction=qrcode.ERROR_CORRECT_L, box_size=10, border=4)
    #qrc = QRcode.qrcode()

    @classmethod
    def create_qrcode(cls, data):
        try:
            cls.qrc.add_data(data)
            cls.qrc.make(fit=True)
            qrcode_image = cls.qrc.make_image(fill_color="black", back_color="white")
            """response = make_response(jsonify({
                "response": {
                    "statusCode": 204,
                    "message": "Success! QR Code was generated",
                    "data": qrcode_image
                }
            }), 204)"""
            return send_file(qrcode_image, mimetype="image/png")
        except Exception as e:
            return make_response(jsonify({
                "response": {
                    "statusCode": 400,
                    "message": f"Error: {e}",
                    "data": []
                }
            }), 400)

