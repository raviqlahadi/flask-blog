from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class RegisterForm(FlaskForm):
    username = StringField('Email', [validators.DataRequired()])
    name = StringField('Name', [validators.DataRequired()])
    password = PasswordField('Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm Password', [validators.DataRequired()])


class LoginForm(FlaskForm):
    username = StringField('Email', [validators.DataRequired()])
    password = PasswordField('Password', [validators.DataRequired()])
