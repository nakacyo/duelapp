from duelapp import app
from flask import render_template

@app.route('/')
def index():
    data1 = "data1"
    return render_template('index.html', data1=data1)

@app.route('/rule')
def rule():
    return render_template('rule.html')

@app.route('/ref')
def ref():
    return render_template('ref.html')