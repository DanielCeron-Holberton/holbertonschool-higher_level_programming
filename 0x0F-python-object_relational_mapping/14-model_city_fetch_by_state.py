#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    elements_to_query = session.query(State.name, City.id, City.name).join(
        City, State.id == City.state_id).order_by(City.id)

    for element in elements_to_query:
        print("{e[0]}: ({e[1]}) {e[2]}".format(e=element))

    session.close()
