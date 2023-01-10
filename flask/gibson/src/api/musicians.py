from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('musicians', __name__, url_prefix='/musicians')


@bp.route('')
def musicians():
    return render_template('sub_musicians.html', title='Gibson Musicians')
