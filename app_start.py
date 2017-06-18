import http

from flask import Flask, abort, jsonify
from sqlalchemyEx import sqlEx
from sqlalchemyEx.models import db
from sqlalchemyEx.models import User

app = Flask(__name__)
app.register_blueprint(sqlEx)
app.config.from_object('settings')

db.init_app(app)


@app.route('/')
def index():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


@app.route('/hello')
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
