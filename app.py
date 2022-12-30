from flask import Flask, render_template
from forms import UrlForm
from cert.extract import Extract
#from validator.validate import Validate

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a very hard to guess secret super key'


@app.route('/', methods=['GET', 'POST'])
def index():
    url = None
    ssl = None
    form = UrlForm()
    if form.validate_on_submit():
        url = form.url.data
        #validate = Validate()
        #if not validate.url(url):
        #    form.url.errors.append(f"url {url} is wrong, enter correct url")
        ssl = Extract()
        ssl = ssl.fetch_ssl(url)
        form.url.data = ''
    return render_template('index.html', form=form, url=url, ssl=ssl)
