from turtle import title
from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('acc', __name__, url_prefix='/acc')


@bp.route('')
def acc():
    return render_template('sub_acc.html', title='Gibson Accessories')
