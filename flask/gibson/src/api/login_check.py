import string
from flask import Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db
from cryptography.fernet import Fernet

bp = Blueprint('login_check', __name__, url_prefix='/login_check')


@bp.route('', methods=['POST'])
def login_check():
    sent_username = request.form['username']
    sent_userpw = request.form['userpw']

    u = User.query.filter_by(username=sent_username).first()
    username = u.username
    password = u.password

    if sent_username == username and sent_userpw == password:
        return sent_username
    else:
        return password
    # return jsonify(u.serialize())

# @bp.route('/<string:id>', methods=['GET'])
# def login_check(id: string):

#     u = User.query.filter_by(username=id).first()

#     return jsonify(u.serialize())
