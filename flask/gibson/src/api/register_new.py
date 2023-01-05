from crypt import methods
from django.shortcuts import render
from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db
import hashlib
import secrets
from cryptography.fernet import Fernet
import bcrypt

# ref: https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/

bp = Blueprint('register_new', __name__, url_prefix='/register_new')


# 1. encode password
def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


def enc(userpw: str):
    # 2. encode password
    # key = Fernet.generate_key()
    # fernet = Fernet(key)
    # enc_pw = fernet.encrypt(userpw.encode())

    # 3. encode password
    # .encode() = Strings must be encoded before hashing
    enc_pw = bcrypt.hashpw(password=userpw.encode(
        'utf-8'), salt=bcrypt.gensalt())
    enc_pw = enc_pw.decode()
    return enc_pw


@bp.route('', methods=['POST'])
def register_new():
    username = request.form['username']
    userpw = request.form['userpw']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    useremail = request.form['useremail']
    usertel = request.form['usertel']
    reg_date = request.form['reg_date']
    guitar_type = request.form['guitar_type']
    city = request.form['city']
    if username == "" or userpw == "" or first_name == "" or last_name == "" or useremail == "" or usertel == "":
        return 'Please fill in the required fields'
    if username in userpw or first_name in userpw or last_name in userpw:
        return 'You can not include your information in your password'
        # this is not working. needed to be editted.
    if len(username) < 3 or len(userpw) < 8:
        return 'Please set at least 3 characters for the ID and at lease 8 numbers of the password'

    # construct User
    u = User(
        username=username,
        # password=scramble(userpw),
        password=enc(userpw),
        first_name=first_name,
        last_name=last_name,
        email=useremail,
        phone=usertel
    )
    if reg_date != "":
        u.reg_date = reg_date
    if guitar_type != "":
        u.guitar_type = guitar_type
    if 'city' != "":
        u.city = city
    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return render_template('index.html', username=username)
