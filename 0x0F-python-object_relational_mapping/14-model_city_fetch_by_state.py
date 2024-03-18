#!/usr/bin/python3
'''
    prints all City objects from the database hbtn_0e_14_usa
'''
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    name, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                            .format(name, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for obj in session.query(
            State.name, City.id, City.name
            ).filter(State.id == City.state_id):
        print(obj[0] + ": (" + str(obj[1]) + ") " + obj[2])
