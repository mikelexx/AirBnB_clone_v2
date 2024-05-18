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


@app.route("/states/<id>")
def state_cities(id):
    """
    returns cities of the specified state id in html template
    """
    states = storage.all(State)
    for key in states:
        if states[key].id == id:
            return render_template("9-states.html",
                                   state=states[key],
                                   id="id_found")
    return render_template("9-states.html", id="id_not_found")


@app.route("/states")
def states():
    """
    returns all states objects in html template
    """
    states = storage.all(State)
    return render_template("9-states.html", states=states, id="no_id")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
