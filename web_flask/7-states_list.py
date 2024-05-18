#!/usr/bin/python3
"""
script that starts a Flask application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sqlalchemy_sessions(exc):
    """
    for closing sqlalchemy after every request
    """
    storage.close()


@app.route("/states_list")
def states_list():
    """
    returns html page for state objects sorted by name [A-Z].
    """
    states = storage.all(State)
    states_list = []
    for key, val in states.items():
        states_list.append(val)
    return render_template('7-states_list.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
