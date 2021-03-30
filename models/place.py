#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import os
import models


class Place(BaseModel, Base):
    """ class Place """
    __tablename__ = "places"
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        reviews = relationship("Review", backref="place",
                               cascade="all, delete")

    else:

        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """ List of place's reviews """
            new_list = []
            recorrido = models.storage.all(Review).items()
            for k, v in recorrido:
                if v.place_id == self.id:
                    lista.append(recorrido[k])
            return new_list
