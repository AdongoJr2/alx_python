#!/usr/bin/python3
"""My module"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """State class
    """
    __tablename__ = "states"

    id = Column(
        Integer,
        unique=True,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)
