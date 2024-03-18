#!/usr/bin/python3
'''
    adds the State object “Louisiana”
    to the database hbtn_0e_6_usa
'''
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
                            username, password, database))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new = State(name='Louisiana')
    session.add(new)
    new_states = session.query(State).filter_by(name='Louisiana').first()
    print(new_states.id)
    session.commit()
