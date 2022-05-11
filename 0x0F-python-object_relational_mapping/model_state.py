#!/usr/bin/python3
"""Module SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Creates a class representing a state object"""

    __tablename__ = 'State'
    id = Column(Integer(11),
                primary_key=True,
                nullable=False,
                autoincrement=True)
    name = Column(String(128), nullable=False)
