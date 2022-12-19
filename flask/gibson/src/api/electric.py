from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('electric', __name__, url_prefix='/electric')


@bp.route('')
def electric():
    return render_template('sub_electric.html')
