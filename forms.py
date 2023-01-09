from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, validators)
from wtforms.validators import InputRequired, Length, ValidationError
from urllib.parse import urlparse

class UrlForm(FlaskForm):
    url = StringField(label = 'Enter website url', render_kw={'placeholder': 'website.com'}, validators=[InputRequired()])

    def validate_url(form, url):
            u = urlparse(url.data)
            if not all([u.scheme, u.netloc]):
                raise ValidationError('Url is not valid, please enter https://example.com')
