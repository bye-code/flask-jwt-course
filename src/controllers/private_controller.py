from flask.views import MethodView
from src.hooks.verify_token import verify_token

class PrivateController(MethodView):

    decorators = [verify_token]

    def get(self):
        return "I'm private controller"
