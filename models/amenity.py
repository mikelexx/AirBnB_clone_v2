#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    describes features of a place
    """
    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        from models.place import place_amenity
        place_amenities = relationship("Place",
                                       back_populates="amenities")
    else:
        name = ""
