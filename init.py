from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


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
