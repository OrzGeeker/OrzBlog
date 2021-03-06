from flask_mail import Message
from app import mail
from flask import render_template, current_app
from threading import Thread
from flask_babel import _

def send_password_reset_mail(user):
    token = user.get_reset_password_token()
    send_mail(_('[Microblog] Reset Your Password'),
              sender = current_app.config['ADMINS'][0],
              recipients= [user.email],
              text_body = render_template('auth/email/reset_password.txt', user=user, token=token),
              html_body = render_template('auth/email/reset_password.html', user=user, token=token))


def send_mail(subject,
              sender,
              recipients,
              text_body,
              html_body,
              attachments=None,
              sync=False):

    msg = Message(subject = subject,
                  sender = sender,
                  recipients=recipients)

    msg.body=text_body
    msg.html=html_body

    if attachments:
        for attachment in attachments:
            msg.attach(*attachment)
    if sync:
        mail.send(msg)
    else:
        Thread(target=send_async_mail,
               args=(current_app._get_current_object(),msg)).start()

def send_async_mail(app,msg):
    with app.app_context():
        mail.send(msg)

