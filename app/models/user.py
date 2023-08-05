from app import db
from uuid import uuid4
from flask_login import UserMixin

def get_uuid():
    return uuid4().hex

class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    email = db.Column(db.String(345), unique=True)
    password = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"{self.email}>"
    
    def get_id(self):
            return str(self.id)