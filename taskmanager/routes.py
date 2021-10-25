from flask import render_template
from taskmanager import app, db
from taskmanager.models import Category, Task


"""Set route function for base.html"""
@app.route("/")
def home():
    return render_template("tasks.html")
