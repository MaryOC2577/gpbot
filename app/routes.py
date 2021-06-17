from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home')

@app.route('/json')
def get_bot_response():
    return render_template('get_bot_response.json')