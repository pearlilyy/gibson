from flask import Flask, render_template, request
import psycopg2  # it imports the psycopg2 package.

# Connect to your postgres DB
conn = psycopg2.connect(
    """
    dbname=gibson user=postgres host=localhost port=5432
    """
)
conn.set_session(autocommit=True)

# Open a cursor to perform database operations
cur = conn.cursor()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/login_check', methods=['post'])
def login_check():
    username = request.form['userid']
    userpw = request.form['userpw']
    return render_template('index.html', username=username)


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/register_new', methods=['post'])
def register_new():
    userid = request.form['userid']
    userpw = request.form['userpw']
    username = request.form['username']
    usertel = request.form['usertel']
    useremail = request.form['useremail']
    guitar = request.form['guitar']
    city = request.form['city']
    regdate = request.form['regdate']
    # return userid, userpw, username, usertel, useremail, guitar, city

    cur.execute('INSERT INTO users VALUES (id, username, password, name, email, phone, regdate, guitar_type, city)', (
        9, userid, userpw, username, useremail, usertel, regdate, guitar, city))
    conn.commit()
    records = cur.fetchall()
    return records


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
