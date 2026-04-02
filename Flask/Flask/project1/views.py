from project1 import app
from flask import render_template, url_for

@app.route('/')
def homepage():
    usuario = 'Jorge'
    idade = 40

    context = {
        'usuario': usuario,
        'idade': idade
    }
    return render_template('index.html', context=context)

@app.route('/contato/')
def newpage():
    return render_template('contato.html')