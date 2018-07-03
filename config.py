import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECREt_KEY') or 'you-will-never-guess'

    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI') or \
    'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER=os.environ.get('MAIL_SERVER') or 'smtp.qq.com'
    MAIL_PORT=int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS') or 1
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME') or '824219521@qq.com'
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD') or 'ifjjerlzkmjcbbbc'
    ADMINS=['824219521@qq.com']

    POSTS_PER_PAGE=25

    
