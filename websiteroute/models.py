from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique = True)
    username = db.Column(db.String(30))
    password = db.Column(db.String(150))
    files = db.relationship("File")
    
# File model

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    display_name = db.Column(db.String(150))
    key = db.Column(db.String(100))
    url = db.Column(db.String(200))
    passkey = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user = db.Column(db.Integer, db.ForeignKey("user.id"))
