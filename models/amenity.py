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
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        """
        from models.place import place_amenity
        place_amenities = relationship("Place",
                                       secondary=place_amenity,
                                       back_populates="amenities")
        """
    else:
        name = ""
