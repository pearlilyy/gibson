from flask import Blueprint, jsonify, abort, request
from ..models import User, Fix, db
import hashlib
import secrets

bp = Blueprint('fix', __name__, url_prefix='/fix')


@bp.route('', methods=['GET'])
def index():
    fix = Fix.query.all()
    result = []
    for f in fix:
        result.append(f.serialize())
    return jsonify(result)


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    f = Fix.query.get_or_404(id)
    return jsonify(f.serialize())


@bp.route('', methods=['POST'])
def create():
    if 'user_id' not in request.json or 'post_id' not in request.json:
        return abort(400)

    f = Fix(
        user_id=request.json['user_id'],
        guitar_info=request.json['guitar_info'],
        attached_file=request.json['attached_file']
    )
    db.session.add(f)
    db.session.commit()
    return jsonify(f.serialize())


@bp.route('/<int:id>/posts/<int:post_id>', methods=['DELETE'])
def delete(id: int, post_id: int):
    f = Fix.query.get_or_404((id))
    try:
        db.session.delete(f)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)
