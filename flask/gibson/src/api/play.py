from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('play', __name__, url_prefix='/play')


@bp.route('')
def play():
    return render_template('sub_play.html', title='Gibson How To Play')
