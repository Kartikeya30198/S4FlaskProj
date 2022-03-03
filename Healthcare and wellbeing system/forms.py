from flask_wtf import Form, FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, RadioField, EmailField, TextAreaField
from wtforms.validators import InputRequired


class LoginForm(Form):
    username = StringField('Username', validators=[InputRequired()])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Login')

class RegistrationForm(Form):
    username = StringField('UserName', validators=[InputRequired()])
    password = PasswordField('PassWord', validators=[InputRequired()])
    retype = PasswordField('Re-PassWord', validators=[InputRequired()])
    "gender = RadioField('Gender',choices=['male','Female','Others'],default='',validators=[InputRequired()])"
    phoneno = StringField('Phone No',validators=[InputRequired()])
    email = EmailField('E-Mail',validators=[InputRequired()])
    "address = StringField('Address')"
    submit = SubmitField('SignUp')
