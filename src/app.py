from flask import Flask, render_template, flash
from forms import UrlForm, SaveCertForm
from cert.extract import Extract

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very hard to guess secret super key'


@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    ssl = None
    visibility = 'hidden'
    check_url_form = UrlForm()
    save_url_form = SaveCertForm()

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

    return render_template('index.html', check_url_form=check_url_form, save_url_form=save_url_form,  url=url, ssl=ssl, visibility=visibility)
