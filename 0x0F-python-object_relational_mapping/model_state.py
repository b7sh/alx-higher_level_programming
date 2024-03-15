#!/usr/bin/python3
'''
ains the class definition of a State and
an instance Base = declarative_base()
'''
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class state(Base):
    '''
    inherits from Base Tips
    links to the MySQL table stat
    attribute:
    id: Integer
    name: String
    '''
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
