#!/usr/bin/python3
"""Module updates a name
"""

from sys import argv
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    state_to_update = session.query(State).filter_by(id=2).first()

    state_to_update.name = "New Mexico"

    session.commit()
    session.close()
