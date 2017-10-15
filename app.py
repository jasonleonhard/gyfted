"""."""
import os
from flask import Flask, render_template
# from flask_sqlalchemy import SQLAlchemy
from models import db, User

app = Flask(__name__)
app.secret_key = "development-key"
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db.init_app(app)


@app.route("/")
def index():
    """Splash screen."""
    return render_template("index.html")


@app.route("/about")
def about():
    """Mission statement."""
    return render_template("about.html")


@app.route("/map")
def map():
    """Stubbed out map and list view."""
    return render_template("map.html")


# disable browser caching
@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame.

    Also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
