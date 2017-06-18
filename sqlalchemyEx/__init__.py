from sqlalchemyEx.model import db, User
from flask import Blueprint, jsonify

sqlEx = Blueprint('sqlalchemyEx', __name__)

@sqlEx.route('/getlist')
def getlist():
    rt = User.query.all()
    return 'getlist'
