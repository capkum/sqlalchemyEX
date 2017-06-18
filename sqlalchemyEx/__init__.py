from sqlalchemyEx.models import User
from flask import Blueprint, jsonify

sqlEx = Blueprint('sqlalchemyEx', __name__)

@sqlEx.route('/getlist')
def getlist():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])



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
