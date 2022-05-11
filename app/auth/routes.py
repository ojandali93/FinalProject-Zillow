from xml.dom import ValidationErr
from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Property
from app.auth.forms import SignupForm, LoginForm

from flask_login import login_required, login_user, logout_user, current_user

from app.extensions import app, db
from app.models import User

auth = Blueprint('auth', __name__)

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
  form = SignupForm()
  if request.method == 'POST':
    if form.validate_on_submit():
      username = request.form.get('username')
      password = request.form.get('password')
      name = request.form.get('name')
      email = request.form.get('email')
      phone = request.form.get('phone')
      user = User(
        username = username,
        password = password,
        name = name,
        email = email,
        phone = phone
      )
      db.session.add(user)
      db.session.commit()
      return redirect(url_for('auth.Login'))
    else:
      raise ValidationErr('There was an issue creating your account')
  else:
    print(form.errors)
    return render_template('signup.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def Login():
  form = LoginForm()
  if request.method == 'POST':
    if form.validate_on_submit():
      user = User.query.filter_by(username = request.form.get('username')).one()
      login_user(user)
      return redirect('main.homepage')
    else:
      raise ValidationErr('Issue Loggin In')
  else:
    print(form.errors)
    return render_template('login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.homepage'))