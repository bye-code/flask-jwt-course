from src.database import db

class User(db.Model):
    __tablename__ = "Users"
    uid = db.Column(db.Integer(), primary_key=True, nullable=False)
    email = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(400), nullable=False)
    name = db.Column(db.String(40), nullable=False)
    last_name = db.Column(db.String(60), nullable=True)

    def __init__(self, email: str=None, password: str=None, name: str=None, last_name: str=None):
        self.email = email
        self.password = password
        self.name = name
        self.last_name = last_name
