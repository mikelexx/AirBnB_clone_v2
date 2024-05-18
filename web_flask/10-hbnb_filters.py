#!/usr/bin/python3
"""
script that starts a Flask application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sqlalchemy_sessions(exc):
    storage.close()


@app.route("/hbnb_filters")
def hbnb_filters():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    amenities_list = []
    states_list = []
    for key, val in states.items():
        states_list.append(val)
    for key, val in amenities.items():
        amenities_list.append(val)
    return render_template("10-hbnb_filters.html",
                           amenities=amenities_list,
                           states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
