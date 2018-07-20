#!/usr/bin/python3
"""
Prints all City objects from the database hbtn_0e_14_usa
"""

if __name__ == '__main__':
    import sys
    from model_state import Base, State
    from model_city import City
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    for c, s in session.query(City, State).\
            order_by(City.id).\
            filter(City.state_id == State.id).\
            all():
        print('{}: ({}) {}'.format(s.name, c.id, c.name))
