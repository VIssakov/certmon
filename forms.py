from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, validators)
from wtforms.validators import InputRequired, Length

class UrlForm(FlaskForm):
    url = StringField('Enter website', validators=[InputRequired()])
