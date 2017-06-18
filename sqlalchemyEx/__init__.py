from sqlalchemyEx.models import User
from flask import Blueprint, jsonify

sqlEx = Blueprint('sqlalchemyEx', __name__)


@sqlEx.route('/getlist')
def getlist():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])
