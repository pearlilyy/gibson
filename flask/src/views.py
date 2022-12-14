from django.shortcuts import render
from django.http import HttpResponse
from models import User, Fix
from flask import Flask, render_template, request

app = Flask(__name__)

# Create your views here.


@app.route('/')
def index():
    users = User.objects.all()
    context = {'users': users}
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
