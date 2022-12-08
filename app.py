import os
from models import db
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# The absolute file directory
base_dir = os.path.abspath(os.path.dirname(__file__))

# making db file in base_dir directory
dbfile = os.path.join(base_dir, 'db.sqlite')

# SQLAlchemy setup

# The DB URL I'm gonna use
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///' + dbfile
# When the business logic ends, run the Commit
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
# The track about the modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# SECRET_KEY
# secret_file = os.path.join(base_dir, 'secrets.json')
# with open(secret_file) as f:
#     secrets = json.loads(f.read())['SECRET_KEY']
app.config['SECRET_KEY'] = 'jqiowejrojzxcovnklqnweiorjqwoijroi'

db.init_app(app)
db.app = app
db.create_all()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
