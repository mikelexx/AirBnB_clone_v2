#!/usr/bin/python3
"""
script that starts a Flask application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sqlalchemy_sessions(exc):
    storage.close()


@app.route("/states_list")
def states_list():
    """
    returns html page for state objects sorted by name [A-Z].
    """


@app.route("/cities_by_states")
def cities_by_states():
    """
    Returns: html page displaying all states and their cities
    """
    states_dict = storage.all(State)
    states_cities = {}
    for key, val in states_dict.items():
        states_cities[val] = val.cities
    return render_template('8-cities_by_states.py', states=states_cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
