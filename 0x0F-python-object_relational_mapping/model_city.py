#!/usr/bin/python3
"""
Creates schema for city class
"""
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


if __name__ == '__main__':
    Base = declarative_base()

    class City(Base):
        __tablename__ = 'cities'
        id = Column(Integer, primary_key=True)
        name = Column(String(128), nullable=False)
        state_id = Column(Integer, ForeignKey('states.id'))
