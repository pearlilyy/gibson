from flask import Blueprint, jsonify, abort, request
from ..models import User, Fix, db
import hashlib
import secrets

bp = Blueprint('users', __name__, url_prefix='/users')


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all()  # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize())  # build list of users as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and ...
    if 'username' not in request.json or 'password' not in request.json or 'first_name' not in request.json or 'last_name' not in request.json or 'email' not in request.json or 'phone' not in request.json:
        return abort(400)

    if len(request.json['username']) < 3 or len(request.json['password']) < 8:
        return abort(400)

    # construct User
    u = User(
        username=request.json['username'],
        password=scramble(request.json['password']),
        first_name=request.json['first_name'],
        last_name=request.json['last_name'],
        email=request.json['email'],
        phone=request.json['phone']
    )
    if 'reg_date' in request.json:
        u.reg_date = request.json['reg_date']
    if 'guitar_type' in request.json:
        u.guitar_type = request.json['guitar_type']
    if 'city' in request.json:
        u.city = request.json['city']
    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)

    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        u.username = request.json['username']
    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = scramble(request.json['password'])
    if 'first_name' in request.json:
        u.first_name = request.json['first_name']
    if 'last_name' in request.json:
        u.last_name = request.json['last_name']
    if 'email' in request.json:
        u.email = request.json['email']
    if 'phone' in request.json:
        u.phone = request.json['phone']
    if 'reg_date' in request.json:
        u.picture = request.json['reg_date']
    if 'guitar_type' in request.json:
        u.guitar_type = request.json['guitar_type']
    if 'city' in request.json:
        u.city = request.json['city']

    try:
        db.session.commit()
        return jsonify(u.serialize())
    except:
        return jsonify(False)


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
