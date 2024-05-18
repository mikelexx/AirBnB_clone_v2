#!/usr/bin/python3
"""
script that starts a Flask web application.
"""
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_hbnb():
    """
    Return: a welcome message
    """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """
    Return: welcome message
    """
    return "HBNB"


@app.route("/c/<text>")
def c_text_display(text):
    """
    Returns: "C" followed by text variable passed.
    """
    text = "C " + " ".join(text.split("_"))
    return text


@app.route("/python/<text>")
@app.route("/python/")
def python_text(text="is cool"):
    """
    Returns: "Python" followed by text variable passed.
    """
    text = "Python " + " ".join(text.split("_"))
    return text


@app.route("/number/<int:n>")
def display_number_only(n):
    """
    Return: the number passed in the url.
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
