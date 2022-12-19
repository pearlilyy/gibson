import datetime
from tkinter import CASCADE
from unicodedata import category
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(300), nullable=False)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    reg_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.datetime.utcnow)
    guitar_type = db.Column(db.String(50), nullable=True)
    city = db.Column(db.String(20), nullable=True)

    def __init__(self, username: str, password: str, first_name: str, last_name: str, email: str, phone: str):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'phone': self.phone,
            'reg_date': self.reg_date.isoformat(),
            'guitar_type': self.guitar_type,
            'city': self.city
        }


class Fix(db.Model):
    __tablename__ = "fix"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    guitar_info = db.Column(db.String(50), nullable=False)
    attached_file = db.Column(db.String(30), nullable=True)
    post_date = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.utcnow)

    def __init__(self, user_id: int, guitar_info: str):
        self.user_id = user_id
        self.guitar_info = guitar_info

    def serialize(self):
        return {
            'user_id': self.user_id,
            'guitar_info': self.guitar_info,
            'attached_file': self.attached_file,
            'post_date': self.post_date
        }


# class Mypage(db.Model):
#     __tablename__ = "mypages"

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
#     introduction = db.Column(db.String(50))

#     def __init__(self, user_id: int, introduction: str):
#         self.user_id = user_id
#         self.introduction = introduction

#     def serialize(self):
#         return {
#             'id': self.id,
#             'user_id': self.user_id,
#             'introduction': self.introduction
#         }
