import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECREt_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_Url') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    
