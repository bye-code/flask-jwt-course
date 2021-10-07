from flask import Flask
from flask_qrcode import QRcode
from src.routes.routes import routes, qrcode_route
from src.database import db
import qrcode

class Application:

    app: Flask

    def __init__(self) -> None:
        self.app = Flask(__name__)
        self.__settings()
        self.__register_routes()
        self.__init_db()
    
    def start(self):
        try:
            self.app.run(self.app.config['HOST'], self.app.config['PORT'], self.app.config['DEBUG'], load_dotenv=True)
        except Exception as e:
            pass

    def __settings(self):
        try:
            self.app.config.from_pyfile('../appconfig.cfg')
            self.app.config.from_mapping(
                SECRET_KEY=self.app.config['SECRET_KEY']
            )
            self.app.config['SQLALCHEMY_DATABASE_URI'] = self.app.config['DATABASE_CONN']
            self.app.config['SQLALCHEMY_TRACK_MODICATIONS'] = True
            db.init_app(self.app)
            #QRcode(self.app) 
        except KeyError as e:
            print("An error ocurred with the configurations")
            raise e
        except Exception as e:
            print("Error")
            raise e

    def __register_routes(self):
        self.app.add_url_rule(routes["index"], view_func=routes["index_controller"], methods=['GET'])
        self.app.add_url_rule(routes["signup"], view_func=routes["signup_controller"], methods=['POST'])
        self.app.add_url_rule(routes["signin"], view_func=routes["signin_controller"], methods=['POST'])
        self.app.add_url_rule(routes["private"], view_func=routes["private_controller"], methods=['GET'])
        self.app.add_url_rule(qrcode_route["qrcode"], view_func=qrcode_route["qrcode_view"], methods=['GET'])


    def __init_db(self):
        db.create_all(app=self.app)
