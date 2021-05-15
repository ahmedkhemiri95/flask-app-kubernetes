from application import app
from flask import Flask,render_template

@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')
