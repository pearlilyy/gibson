import hashlib
import secrets
from flask import Flask, render_template, abort, jsonify, request
from models import User, Fix, db

app = Flask(__name__)


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_check', methods=['post'])
def login_check():
    username = request.form['username']
    userpw = request.form['userpw']
    return render_template('index.html', username=username)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register_new', methods=['POST'])
def register_new():
    username = request.form['username']
    userpw = request.form['userpw']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    useremail = request.form['useremail']
    usertel = request.form['usertel']
    reg_date = request.form['reg_date']
    guitar_type = request.form['guitar_type']
    city = request.form['city']
    if username == "" or userpw == "" or first_name == "" or last_name == "" or useremail == "" or usertel == "":
        return 'Please fill up the required contents'
    if len(username) < 3 or len(userpw) < 8:
        # return abort(400)
        return 'Please set at least 3 characters for the ID and at lease 8 numbers of the password'

    # construct User
    u = User(
        username=username,
        password=scramble(userpw),
        first_name=first_name,
        last_name=last_name,
        email=useremail,
        phone=usertel
    )
    if reg_date != "":
        u.reg_date = reg_date
    if guitar_type != "":
        u.guitar_type = guitar_type
    if 'city' != "":
        u.city = city
    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement
    return f'{username}You are successfully registered!'
    # userid = request.form['userid']
    # userpw = request.form['userpw']
    # username = request.form['username']
    # usertel = request.form['usertel']
    # useremail = request.form['useremail']
    # guitar = request.form['guitar']
    # city = request.form['city']
    # regdate = request.form['regdate']
    # return f'Nice to meet you {username}'


@app.route('/acc')
def acc():
    return render_template('sub_acc.html')


@app.route('/acoustic')
def acoustic():
    return render_template('sub_acoustic.html')


@app.route('/dealers')
def dealers():
    return render_template('sub_dealers.html')


@app.route('/electric')
def electric():
    return render_template('sub_electric.html')


@app.route('/faq')
def faq():
    return render_template('sub_FAQ.html')


@app.route('/feature')
def feature():
    return render_template('sub_feature.html')


@app.route('/fix')
def fix():
    return render_template('sub_fix.html')


@app.route('/history')
def history():
    return render_template('sub_history.html')


@app.route('/maintaining')
def maintaining():
    return render_template('sub_maintaining.html')


@app.route('/musicians')
def musicians():
    return render_template('sub_musicians.html')


@app.route('/news')
def news():
    return render_template('sub_news.html')


@app.route('/play')
def play():
    return render_template('sub_play.html')


@app.route('/rent')
def rent():
    return render_template('sub_rent.html')


if __name__ == '__main__':
    app.run(debug=True)
