from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('rent', __name__, url_prefix='/rent')


@bp.route('')
def rent():
    return render_template('sub_rent.html', title='Gibson Guitar Rent')
