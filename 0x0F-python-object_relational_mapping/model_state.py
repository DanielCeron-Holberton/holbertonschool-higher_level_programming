#!/usr/bin/python3
"""Module SQLAlchemy"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Creates a class representing a state object"""
    __tablename__ = 'state'
    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(240), nullable=False)
