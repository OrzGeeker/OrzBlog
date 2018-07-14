from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l

from app.models import User

from wtforms import StringField
from wtforms import TextAreaField
from wtforms import SubmitField
from wtforms.validators import DataRequired
from wtforms.validators import ValidationError
from wtforms.validators import Length

from flask import request

class SearchForm(FlaskForm):
    q=StringField(_l('Search'),validators=[DataRequired()])

    def __init__(self,*args,**kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata']=request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled']=False

        super(SearchForm,self).__init__(*args,**kwargs)

class EditProfileForm(FlaskForm):
    username=StringField(_l('Username'), validators=[DataRequired()])
    about_me=TextAreaField(_l('About me'), validators=[Length(min=0, max=140)])
    submit= SubmitField(_l('Submit'))

    def __init__(self,original_username, *args, **kwargs):
        super(EditProfileForm,self).__init__(*args,**kwargs)
        self.original_username=original_username


    def validate_username(self,username):
        if username.data != self.original_username:
            user=User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')

class PostForm(FlaskForm):
    post = TextAreaField(_l('Say something'), validators = [DataRequired(), Length(min=1, max=140)])
    submit = SubmitField(_l('Submit'))


class MessageForm(FlaskForm):
    message =  TextAreaField(_l('Message'), validators=[DataRequired(),Length(min=0,max=140)])
    submit=SubmitField(_l('Submit'))
