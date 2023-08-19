#!/usr/bin/python3
"""My module"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(
            username,
            password,
            db_name
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    try:
        result = session.query(
            State
        ).order_by(
            State.id.asc()
        ).one()

        print("{}: {}".format(result.id, result.name))
    except:
        print("Nothing")
