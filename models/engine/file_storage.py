#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.state import State
import json

classes = {
    "User": User,
    "Place": Place,
    "State": State,
    "Review": Review,
    "City": City,
    "Amenity": Amenity
}


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            objects = {}
            if type(cls) is str and cls in classes:
                for key, obj in self.__objects.items():
                    if key.split('.')[0] == cls:
                        objects.update({key: obj})
            elif cls.__name__ in classes:
                for key, obj in FileStorage.__objects.items():
                    if key.split('.')[0] == cls.__name__:
                        objects.update({key: obj})
            return objects
        print()
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary
        dict.update() inserts specified objects to the dictionary
        Args: obj (object) : object to update
        """
        dict_obj = obj.to_dict()
        self.all().update({dict_obj['__class__'] + '.' + obj.id: obj})

    def save(self):
        """
        Saves  file objects to filestorage
        """

        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def delete(self, obj=None):
        """ delete obj from __objects if it’s inside - if obj is equal to
        None, the method should not do anything
        Args:
            obj (object): object to delete
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + str(obj.id)
            if key in self.__objects:
                del FileStorage.__objects[key]
        self.save()

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    # constructs class object from json
                    FileStorage.__objects[key] = classes[val['__class__']](
                        **val)
        except FileNotFoundError:
            pass
