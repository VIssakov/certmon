from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)
from wtforms.validators import InputRequired, ValidationError
from urllib.parse import urlparse

class UrlForm(FlaskForm):
    url = StringField(label = 'Enter website url', render_kw={'placeholder': 'website.com'}, validators=[InputRequired()])
    check = SubmitField()

    def validate_url(form, url):
            u = urlparse(url.data)
            if not all([u.scheme, u.netloc]):
                raise ValidationError('Url is not valid, please enter https://example.com')
