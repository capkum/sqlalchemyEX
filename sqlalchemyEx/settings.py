SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://flask:flask123@localhost/flask_ex?charset=utf8' 
SQLALCHEMY_TRACK_MODIFICATIONS = False

try:
    from sqlalchemyEx.local_settings import *  # noqa
except ImportError:
    pass
