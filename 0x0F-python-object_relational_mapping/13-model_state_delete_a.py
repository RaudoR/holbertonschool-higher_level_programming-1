#!/usr/bin/python3
"""deletes all State objects with a name containing the
letter a from the database
Args:
    mysql username: name of the user
    mysql password: password for database
    database name: name of the database
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    state = session.query(State).filter_by(id='2').first()
    state.name = "New Mexico"
    session.commit()
    session.close()
