from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db
import hashlib
import secrets

bp = Blueprint('login', __name__, url_prefix='/login')


@bp.route('')
def login():
    return render_template('login.html')
