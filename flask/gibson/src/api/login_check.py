from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db
import hashlib
import secrets

bp = Blueprint('login_check', __name__, url_prefix='/login_check')


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


@bp.route('', methods=['POST'])
def login_check():
    username = request.form['username']
    userpw = scramble(request.form['userpw'])
    return render_template('index.html', username=username)
