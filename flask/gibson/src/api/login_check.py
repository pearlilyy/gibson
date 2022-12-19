from crypt import methods
from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('login_check', __name__, url_prefix='/login_check')


@bp.route('')
def login_check():
    username = request.form['username']
    userpw = request.form['userpw']

    users = User.query.all()
    result = []
    for u in users:
        result.append(u.serialize())
    return jsonify(result)
