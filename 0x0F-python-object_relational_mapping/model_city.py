#!/usr/bin/python3
'''
    file similar to model_state.py named model_city.py
    that contains the class definition of a City
'''
from sqlalchemy import Integer, String, Column, ForeignKey
from model_state import Base


class City(Base):
    '''
        class attribute:
        id: integer
        name: string
        state_id: integer
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state_id'), nullable=False)
