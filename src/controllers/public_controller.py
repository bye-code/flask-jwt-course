from flask import request
from flask.views import MethodView

class IndexController(MethodView):

    def get(self):
        return "I'm public controller"
