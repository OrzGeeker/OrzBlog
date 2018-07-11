from flask import Flask
from flask import request
from config import Config

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel
from flask_babel import lazy_gettext as _l

import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os

app = Flask(__name__)

app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app,db)
mail = Mail(app)
bootstrap=Bootstrap(app)
moment=Moment(app)
babel=Babel(app)

login = LoginManager(app)
login.login_view = 'auth.login'
login.login_message=_l('Please log in to access this page.')

if not app.debug:

    # Error send email
    if app.config['MAIL_SERVER']:
        auth=None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth=(app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure=()

        host=(app.config['MAIL_SERVER'],app.config['MAIL_PORT'])
        fromaddr=app.config['MAIL_USERNAME']
        toaddrs=app.config['ADMINS']
        title='Microblog Failure'
        credentials=auth

        mail_handler=SMTPHandler(
            mailhost=host,
            fromaddr=fromaddr,
            toaddrs=toaddrs,
            subject=title,
            credentials=auth,
            secure=secure,
            timeout=5.0
            )

        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


    # Error log into file
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler=RotatingFileHandler('logs/microblog.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

@babel.localeselector
def get_locale():
   return request.accept_languages.best_match(app.config['LANGUAGES'])


from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app.auth import bp as auth_bp
app.register_blueprint(auth_bp, url_prefix='/auth')

from app.main import bp as main_bp
app.register_blueprint(main_bp, url_prefix='/main')

from app import  models


