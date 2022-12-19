from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('maintaining', __name__, url_prefix='/maintaining')


@bp.route('')
def maintaining():
    return render_template('sub_maintaining.html')
