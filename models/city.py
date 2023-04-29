#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    state_id = column(string(60), nullable=False, ForeignKey('state.id'))
    name = column(string(128), nullable=False)
