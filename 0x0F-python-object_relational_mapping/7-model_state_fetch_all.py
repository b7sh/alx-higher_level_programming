#!/usr/bin/python3
''' lists all State objects from the database hbtn_0e_6_usa '''
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main":
    username, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for obj in session.query(state).order_by(state.id):
        print(obj.id, obj.name, sep=': ')
