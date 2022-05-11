# Create your models here.
"""Create database models to represent tables."""
from app.extensions import db
from sqlalchemy.orm import backref

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String)
  username = db.Column(db.String)
  password = db.Column(db.String)
  email = db.Column(db.String)
  phone = db.Column(db.Integer)

class Property(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  address = db.Column(db.String)
  beds = db.Column(db.Integer)
  baths = db.Column(db.Integer)
  sqft = db.Column(db.Integer)
  price = db.Column(db.Integer)
  status = db.Column(db.Integer)

favorite_property_table = db.Table('favorite',
  db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
  db.Column('property_id', db.Integer, db.ForeignKey('property.id'))
)