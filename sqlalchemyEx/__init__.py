from sqlalchemyEx.model import db, User
from flask import Blueprint, jsonify, request

sqlEx = Blueprint('sqlalchemyEx', __name__)


@sqlEx.route('/getlist')
def getlist():
    rt = User.query.all()
    return 'getlist'


@sqlEx.route('/User', methods=['POST'])
def create():
    try:
        _username = request.values.get('username')
        _email = request.values.get('email')

        create = User(_username, _email)
        db.session.add(create)
        db.session.commit()

    except Exception as e:
        print(str(e))

    return 'post'


@sqlEx.route('/User/<int:userid>', methods=['PUT'])
def update(userid):

    try:
        _username = request.values.get('username')
        _email = request.values.get('email')

        User.query.filter_by(id=userid).update({
            'username': _username,
            'email': _email
        })
        db.session.commit()

    except Exception as e:
        print(str(e))

    return 'update'


@sqlEx.route('/User/<int:userid>', methods=['DELETE'])
def delete(userid):
    try:
        user = User.query.filter_by(id=userid).first()

        if user is not None:
            db.session.delete(user)
            db.session.commit()
            return 'delete complite'
        else:
            return 'false delete'

    except Exception as e:
        print(str(e))

    return 'delete'
