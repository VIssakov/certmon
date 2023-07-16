import os
from flask import Flask, render_template, flash
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
    subject = db.Column(db.String(100), nullable=False)
    not_before = db.Column(db.String(100), nullable=False)
    not_after = db.Column(db.String(100), unique=True, nullable=False)
    issuer = db.Column(db.String(100), nullable=False)
    extension_count = db.Column(db.String(100), nullable=False)
    subject_altName = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<Certificate {self.subject}>'


@app.before_request
def create_tables():
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
            print(save_url_form.subject.data)
            flash('success')
        if save_url_form.cancel.data:
            visibility = 'hidden'
            flash('cancel')

    return render_template('index.html', check_url_form=check_url_form, save_url_form=save_url_form,  url=url, ssl=ssl, visibility=visibility, certificates=certificates)
