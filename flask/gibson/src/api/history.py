from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('history', __name__, url_prefix='/history')


@bp.route('')
def history():
    return render_template('sub_history.html', title='Gibson History')
