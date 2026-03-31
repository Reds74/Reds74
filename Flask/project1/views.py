from project1 import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/contato/')
def newpage():
    return 'Outra VIEW!!'