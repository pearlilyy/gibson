from flask import Flask, render_template, request
import sys
# absolute_route = sys.path.append(['gibson/flask'])
# import requests

app = Flask(__name__)


@app.route('/')
def init():
    return 'Welcome to Gibson!'


@app.route('/hello')
def hello():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
