#!/usr/bin/python3
"""
script that starts a Flask application.
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
from os import getenv

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_sqlalchemy_sessions(exc):
    storage.close()


@app.route("/hbnb")
def hbnb():
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    users_list = []
    places_list = []
    amenities_list = []
    states_list = []
    for key, val in states.items():
        states_list.append(val)
    for key, val in amenities.items():
        amenities_list.append(val)
    for key, val in places.items():
        places_list.append(val)
    return render_template("100-hbnb.html",
                           places=places_list,
                           amenities=amenities_list,
                           states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
