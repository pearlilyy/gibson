from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('dealers', __name__, url_prefix='/dealers')


@bp.route('')
def dealers():
    return render_template('sub_dealers.html')
