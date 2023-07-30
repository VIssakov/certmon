from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, validators, SubmitField)
from wtforms.validators import InputRequired, Length, ValidationError
from urllib.parse import urlparse

class UrlForm(FlaskForm):
    url = StringField(label = 'Enter website url', render_kw={'placeholder': 'website.com'}, validators=[InputRequired()])
    check = SubmitField()

    def validate_url(form, url):
            u = urlparse(url.data)
            if not all([u.scheme, u.netloc]):
                raise ValidationError('Url is not valid, please enter https://example.com')

class SaveCertForm(FlaskForm):
    name = StringField(label = 'name')
    subject = StringField(label = 'subject')
    notbefore = StringField(label = 'notBefore')
    notafter = StringField(label = 'notAfter')
    issuer = StringField(label = 'issuer')
    subjectaltname = StringField(label = 'subjectAltName')
    save = SubmitField()
    cancel = SubmitField()
