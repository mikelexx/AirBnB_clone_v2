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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
