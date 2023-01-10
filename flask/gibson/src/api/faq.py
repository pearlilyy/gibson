from flask import Flask, Blueprint, jsonify, abort, render_template, request
from ..models import User, Fix, db

bp = Blueprint('faq', __name__, url_prefix='/faq')


@bp.route('')
def faq():
    return render_template('sub_faq.html', title='Gibson Frequently Asked Questions')
