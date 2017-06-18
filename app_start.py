import http

from flask import Flask, abort, jsonify
from sqlalchemyEx import sqlEx
from sqlalchemyEx.models import db
from sqlalchemyEx.models import User

app = Flask(__name__)
app.register_blueprint(sqlEx)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ok1234@localhost/flask?charset=utf8'  # noqa

db.init_app(app)


@app.route('/')
def hello():
    user = User('Test name', 'test@email.com')
    db.session.add(user)

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        abort(http.client.INTERNAL_SERVER_ERROR, e)

    return jsonify(user.to_dict())


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='localhost', port=8000)
