from src.controllers.private_controller import PrivateController
from src.controllers.public_controller import IndexController
from src.controllers.signup_controller import SignupController
from src.controllers.signin_controller import SigninController

routes: dict = {
    "index": "/api/public", "index_controller": IndexController.as_view("index"),
    "signup": "/api/signup", "signup_controller": SignupController.as_view("signup"),
    "signin": "/api/signin", "signin_controller": SigninController.as_view("signin"),
    "private": "/api/private", "private_controller": PrivateController.as_view("private")
}
