#!/usr/bin/python3
""" turns model to package"""
import os
from models.state import State
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.place import Place
from models.base_model import BaseModel

"""This module instantiates an object of class FileStorage
or Database storage accoring to storage type in the environment"""
if os.getenv("HBNB_TYPE_STORAGE") == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
