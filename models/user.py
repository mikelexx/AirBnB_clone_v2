#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from models.review import Review
from models.place import Place
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'users'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
       # places = relationship("Place",
         #                     back_propagates="user",
    #                          cascade="all, delete-orphan")
        #reviews = relationship("Review",
      #                         backref="user",
     #                          cascade="all, delete-orphan")

    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
    def __init__(self, *args, **kwargs):
        """initialize user object"""
        super().__init__(*args, **kwargs)
