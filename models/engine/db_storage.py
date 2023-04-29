#!/usr/bin/python3
"""
This module defines a class to manage database storage for hbnb clone
"""


from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker


classes = {
            'State': State, 'City': City
          }


class DBStorage:
    """
        Database storage Class
        engine: sqlalchemy engine (mysql, mysqldb)
        session: sqlalchemy session
    """
    __engine = None
    __session = None

    def __init__(self):
        """ Initiallized database storage"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv("HBNB_MYSQL_PWD")
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        HBNB_ENV = getenv('HBNB_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB),
                                      pool_pre_ping=True)

        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query database, return the object or all objects"""
        temp_dict = {}

        for local_cls in classes:
            if cls is None or cls is classes[local_cls] or cls is local_cls:
                obj = self.__session.query(classes[local_cls]).all()
                for objs in obj:
                    key = objs.__class__.__name__ + "." + objs.id
                    temp_dict[key] = objs
        return temp_dict

    def new(self, obj):
        """ Adds obj to current sql session"""
        self.__session.add(obj)

    def save(self):
        """ Commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete specified obj from current session"""
        if obj is None:
            pass
        else:
            self.__session.delete(obj)

    def reload(self):
        """ Reload all database from dbserver"""
        Base.metadata.create_all(self.__engine)
        sessionFact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sessionFact)
        self.__session = Session
