#!/usr/bin/python3
"""
For connecting the models with the preffered database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.state import State
import os

database = os.getenv("HBNB_MYSQL_DB")
host = os.getenv("HBNB_MYSQL_HOST")
username = os.getenv("HBNB_MYSQL_USER")
password = os.getenv("HBNB_MYSQL_PWD")

classes = {
    "User": User,
    "Place": Place,
    "State": State,
    "Review": Review,
    "City": City,
    "Amenity": Amenity
}


class DBStorage:
    """
    This class is for determining how the models connect and\
            interact with the database.
    """
    __engine = None
    __session = None

    def __init__(self):
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            username, password, host, database),
                                      pool_pre_ping=True)

    def all(self, cls=None):
        """
        query on the current database session (self.__session) all
        objects depending of the class name (argument cls)
        Args:
            cls (obj): class for using to apply query filter
        Returns: a dictionary where key =<class-name>.<object-id> and\
                value = object
        """
        dictionary = {}
        if cls is not None:
            if type(cls) is str and cls in classes:
                db_cls_objects = self.__session.query(classes[cls])
                for obj in db_cls_objects.all():
                    if hasattr(obj, '_sa_instance_state'):
                        delattr(obj, '_sa_instance_state')
                    if hasattr(obj, '_sa_instance_state'):
                        print("fuck it did not delete sa")
                    dictionary.update(
                        {obj.__class__.__name__ + '.' + obj.id: obj})

            elif cls in classes.values():
                # if actual class was passed
                db_cls_objects = self.__session.query(cls)
                for obj in db_cls_objects.all():
                    if hasattr(obj, '_sa_instance_state'):
                        delattr(obj, '_sa_instance_state')
                    dictionary.update(
                        {obj.__class__.__name__ + '.' + obj.id: obj})
        else:
            for key in classes:
                objects = self.__session.query(classes[key]).all()
                for obj in objects:
                    if hasattr(obj, '_sa_instance_state'):
                        delattr(obj, '_sa_instance_state')
                    dictionary.update(
                        {obj.__class__.__name__ + '.' + obj.id: obj})

        return dictionary

    def new(self, obj):
        """
        add the object to the current database session (self.__session)
        """
        if obj is not None:

            self.__session.add(obj)

    def save(self):
        """
        commit all changes of the current database session (self.__session)
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        delete from the current database session obj if not None
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database (feature of SQLAlchemy)
        """

        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
