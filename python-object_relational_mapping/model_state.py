#!/usr/bin/python3
"""Has class definition of a State and an instance Base = declaratvie_base()"""


from sqlalchemy import column, Integer, String
from sqlalchemy.ext.declaratvie import declarative_base

Base = declarative_base()


class State(Base):
    """class that inherits from Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullabel=False)
