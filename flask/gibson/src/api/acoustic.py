from turtle import title
from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('acoustic', __name__, url_prefix='/acoustic')


@bp.route('')
def acoustic():
    return render_template('sub_acoustic.html', title='Gibson Acoustic Guitars')
