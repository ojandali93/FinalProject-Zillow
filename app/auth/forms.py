from xml.dom import ValidationErr
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length

from app.models import User

class SignupForm(FlaskForm):
  username = StringField('Username: ', validators=[DataRequired(), Length(min=3, max=50)])
  password = PasswordField('Password: ', validators=[DataRequired()])
  name = StringField('Name: ', validators=[DataRequired()])
  email = StringField('Email: ', validators=[DataRequired()])
  phone = IntegerField('Phone: ', validators=[DataRequired()])
  submit = SubmitField('Sign Up')

  def validate_username(self, username, password):
    user = User.query.filter_by(username=username.data).first()
    if user:
      raise ValidationErr('That username is taken.')

class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(min=3, max=50)])
  password = PasswordField('Password', validators=[DataRequired()])
  submit = SubmitField('Sign Up')

  def validate_username(self, username):
    user = User.query.filter_by(username=username.data)
    if not user:
      raise ValidationErr('No user with that username. Please try again.')

  # def validate_password(self, password):
  #     user = User.query.filter_by(username=self.username.data)
  #     if user and user.data.password:
  #         raise ValidationErr('Password doesn\'t match. Please try again.')