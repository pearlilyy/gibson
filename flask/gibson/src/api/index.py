from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db
import hashlib
import secrets

bp = Blueprint('index', __name__, url_prefix='/')


@bp.route('')
def index():
    result = []
    return render_template('index.html')
