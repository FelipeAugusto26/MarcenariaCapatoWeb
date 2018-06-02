from web_marcenaria import app
from flask import render_template


@app.route('/')
def login():
    return render_template('acess.html')

@app.route('/sistem-home')
def home():
    return render_template('base.html')


@app.route('/')
def orcamento():
    return ''