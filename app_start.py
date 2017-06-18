from flask import Flask
from sqlalchemyEx import db, sqlEx

app = Flask(__name__)
app.register_blueprint(sqlEx)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://flask:flask123@localhost/flask_ex?charset=utf8'

db.init_app(app)


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='localhost', port=8000)
