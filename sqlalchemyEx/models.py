import uuid

from sqlalchemyEx.base import db
from sqlalchemy.orm import class_mapper


class ToDictMixin(object):
    def to_dict(self):
        mapper = class_mapper(self.__class__)
        ret = {}
        for column in mapper.columns:
            value = getattr(self, column.name)
            if isinstance(value, uuid.UUID):
                value = str(value)
            ret[column.name] = value
        return ret


class User(db.Model, ToDictMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username
