#coding="UTF8"
from . import app
from flask import render_template
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/project')
def project():
    return render_template('project.html')
