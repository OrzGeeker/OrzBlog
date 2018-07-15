import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir,'.env'))

class Config(object):
    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    POSTS_PER_PAGE=25
    LANGUAGES=['zh','en']
    ADMINS=['824219521@qq.com']
    ELASTICSEARCH_URL=os.environ.get('ELASTICSEARCH_URL')

    SECRET_KEY = os.environ.get('SECRET_KEY')
    MAIL_SERVER= os.environ.get('MAIL_SERVER')
    MAIL_PORT=int(os.environ.get('MAIL_PORT'))
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS')
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')

    REDIS_URL=os.environ.get('REDIS_URL') or 'redis://'


