#!/usr/bin/python3
"""Adds State object to the database hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = 'Louisiana'

    new_state = State(name=state_name)
    session.add(new_state)
    session.commit()

    states = session.query(State).order_by(State.id)
    for state in states:
        if state.name == state_name:
            print(state.id)
