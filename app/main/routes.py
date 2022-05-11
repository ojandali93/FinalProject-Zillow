from flask import Blueprint, render_template, request, redirect, url_for
from app.models import Property
from app.main.forms import PropertyForm

from flask_login import login_required

from app.extensions import app, db

main = Blueprint('main', __name__)

@main.route('/', methods=['GET'])
def homepage():
  all_properties = Property.query.all()
  print(all_properties)
  return render_template('home.html', all_properties=all_properties)

@main.route('/property/<property_id>', methods=['GET'])
def singleproperty(property_id):
  print(property_id)
  property = Property.query.filter_by(id=property_id).first()
  print(property)
  return render_template('homedetails.html', property=property)

@main.route('/property/new', methods=['GET', 'POST'])
@login_required
def createProperty():
  form = PropertyForm()
  if request.method == 'POST':
    print('create property')
    address = request.form.get('address')
    beds = request.form.get('beds')
    baths = request.form.get('baths')
    sqft = request.form.get('sqft')
    price = request.form.get('price')
    status = request.form.get('status')
    item = Property(
      address = address,
      beds = beds,
      baths = baths, 
      sqft = sqft,
      price = price,
      status = status
    )
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('main.homepage'))
  else:
    return render_template('createproperty.html')