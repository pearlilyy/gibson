import string
from flask import Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db
import bcrypt

bp = Blueprint('login_check', __name__, url_prefix='/login_check')


@bp.route('', methods=['GET', 'POST'])
def login_check():
    # the data sent by the form through html
    sent_username = request.form['username']
    sent_userpw = request.form['userpw']

    # selecting data with username
    u = User.query.filter_by(username=sent_username).first()
    username = u.username
    saved_password = u.password

    # decrypting the password
    pw_chk = bcrypt.checkpw(sent_userpw.encode(
        'utf-8'), saved_password.encode())
    if sent_username == username and pw_chk == True:
        return render_template('index.html', username=sent_username)
    else:
        return f'The user information is not matching for {sent_username}!'

# if you send the id directly to the query string.
# @bp.route('/<string:id>', methods=['GET'])
# def login_check(id: string):
#     u = User.query.filter_by(username=id).first()
#     return jsonify(u.serialize())
