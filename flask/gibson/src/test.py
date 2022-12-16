from django.shortcuts import render
from django.http import HttpResponse
from models import User, Fix, db
from flask import Flask, render_template, Blueprint, jsonify, abort, request

app = Flask(__name__)

# Create your views here.
bp = Blueprint('index', __name__, url_prefix='/')


# @app.route('/')
# def index():
#     users = User.objects.all()
#     context = {'users': users}
#     return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
