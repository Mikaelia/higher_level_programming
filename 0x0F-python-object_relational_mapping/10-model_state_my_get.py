#!/usr/bin/python3
"""Lists State objects containing 'a' from the database hbtn_0e_6_usa
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
    count = 0

    states = session.query(State).order_by(State.id)
    for state in states:
        if state.name == argv[4]:
            print(state.id)
            count+=1
    if not count:
        print('Not found')
