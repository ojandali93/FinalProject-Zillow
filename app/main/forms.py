from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length

class PropertyForm(FlaskForm):
  address = StringField("Address: ", validators=[DataRequired()])
  beds = IntegerField("Beds: ", validators=[DataRequired()])
  baths = IntegerField('Baths: ', validators=[DataRequired()])
  sqfrt = IntegerField("Sqft: ", validators=[DataRequired()])
  price = IntegerField("Price: ", validators=[DataRequired()])
  status = SelectField("Status: ", choices=['Active', 'Coming Soon', 'Pending', 'Sold'])
  submit = SubmitField("Submit")