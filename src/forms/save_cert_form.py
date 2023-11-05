from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)

class SaveCertForm(FlaskForm):
    name = StringField(label = 'name')
    subject = StringField(label = 'subject')
    notbefore = StringField(label = 'notBefore')
    notafter = StringField(label = 'notAfter')
    issuer = StringField(label = 'issuer')
    subjectaltname = StringField(label = 'subjectAltName')
    save = SubmitField()
    cancel = SubmitField()
