from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('news', __name__, url_prefix='/news')


@bp.route('')
def news():
    return render_template('sub_news.html', title='Gibson News')
