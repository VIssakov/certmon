import os
import sys
from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from forms import UrlForm, SaveCertForm
from cert.extract import Extract

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very hard to guess secret super key'
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Certs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    subject = db.Column(db.String(500), nullable=False)
    not_before = db.Column(db.String(100), nullable=False)
    not_after = db.Column(db.String(100), nullable=False)
    issuer = db.Column(db.String(500), nullable=False)
    extension_count = db.Column(db.String(1000), nullable=True)
    subject_altName = db.Column(db.String(1000), nullable=False)

    def __repr__(self):
        return f'<Certificate {self.subject}>'


@app.before_request
def create_tables():
    #db.drop_all()
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    ssl = None
    visibility = 'hidden'
    check_url_form = UrlForm()
    save_url_form = SaveCertForm()
    certificates = Certs.query.all()

    if check_url_form.validate_on_submit():
        url = check_url_form.url.data
        ssl = Extract()
        ssl = ssl.fetch_ssl(url)
        check_url_form.url.data = ''

        if ssl:
            visibility = 'visible'

    if save_url_form.validate_on_submit():
        if save_url_form.save.data:
            check_cert = Certs.query.filter_by(name=save_url_form.name.data).first()
            if check_cert:
                flash('Cert exist in DB')
            else:
                cert_data = Certs(
                    name=save_url_form.name.data,
                    subject=save_url_form.subject.data,
                    not_before=save_url_form.notbefore.data,
                    not_after=save_url_form.notafter.data,
                    issuer=save_url_form.issuer.data,
                    subject_altName=save_url_form.subjectaltname.data
                )
                db.session.add(cert_data)
                db.session.commit()
                flash('success')
                certificates = Certs.query.all()
        if save_url_form.cancel.data:
            visibility = 'hidden'
            flash('cancel')

    return render_template('index.html', check_url_form=check_url_form, save_url_form=save_url_form,  url=url, ssl=ssl, visibility=visibility, certificates=certificates)


@app.post('/<int:cert_id>/delete/')
def delete(cert_id):
    certificate = Certs.query.get_or_404(cert_id)
    db.session.delete(certificate)
    db.session.commit()
    return redirect(url_for('index'))
