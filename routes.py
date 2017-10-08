"""."""
from flask import Flask, render_template

app = Flask(__name__)
app.secret_key = "development-key"


@app.route("/")
def index():
    """."""
    return render_template("index.html")


@app.route("/about")
def about():
    """."""
    return render_template("about.html")


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
