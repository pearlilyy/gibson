from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db
import hashlib
import secrets

bp = Blueprint('register', __name__, url_prefix='/register')


@bp.route('')
def register():
    return render_template('register.html')
