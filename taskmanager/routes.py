from flask import render_template
from taskmanager import app, db


"""Set route function for base.html"""
@app.route("/")
def home():
    return render_template("base.html")
