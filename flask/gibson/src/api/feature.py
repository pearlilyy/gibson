from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('feature', __name__, url_prefix='/feature')


@bp.route('')
def feature():
    return render_template('sub_feature.html')
