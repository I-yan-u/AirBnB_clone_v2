#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    __tablename__ = ''
    name = column(string(128), nullable=False)
    cities = relationship("City", backref="state")
