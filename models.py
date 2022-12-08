import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from test import engine, Base

db = SQLAlchemy()
# Reference:
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/
# https://docs.sqlalchemy.org/en/14/core/metadata.html#sqlalchemy.schema.Column
# https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/#many-to-many-relationships

# register

# app = Flask()
# app.config["SQLALCHEMY_DATABASE_URL"] = 'postgresql://postgres@localhost:5432/gibson'
# db.init_app(app)


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(15), nullable=False, unique=True)
    password = db.Column(db.String(15), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    reg_date = db.Column(db.DateTime, nullable=False,
                         default=datetime.datetime.utcnow)

    def __init__(self, username: str, password: str, name: str, email: str, phone: str):
        self.username = username
        self.password = password
        self.name = name
        self.email = email
        self.phone = phone

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'reg_date': self.reg_date.isoformat()
        }

# FAQ


class Question(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.id'), nullable=False)
    content = db.Column(db.String(300), nullable=False)

    def __init__(self, user_id: int, content: int):
        self.user_id = user_id
        self.content = content

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'content': self.content
        }

# fix request


class Fix(db.Model):
    __tablename__ = "fix"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    phone = db.Column(db.String(20), nullable=False)
    detail = db.Column(db.String(300), nullable=False)
    # attachment = db.Cloumn(db.String())

    def __init__(self, user_id: int, detail: str):
        self.user_id = user_id
        self.detail = detail

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'introduction': self.introduction
        }

# guitar rental


class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    location = db.Column(db.String(50))
    post_date = db.Column(db.DateTime, nullable=False,
                          default=datetime.datetime.utcnow)

    def __init__(self, user_id: int, note: str, photo: str, location: str):
        self.user_id = user_id
        self.note = note
        self.photo = photo
        self.location = location

    def serialize(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'note': self.note,
            'photo': self.photo,
            'location': self.location,
            'post_date': self.post_date.isoformat()
        }

# Base.metadata.create_all(engine)
