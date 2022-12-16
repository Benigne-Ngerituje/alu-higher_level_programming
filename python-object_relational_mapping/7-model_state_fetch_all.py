##!/usr/bin/python3
"""
This script retrieves all state objects from a MySQL database and prints their
ID and name fields to the console.

To run the script, provide the following parameters at the command line:
 - username: the username to use when connecting to the MySQL database
 - password: the password to use when connecting to the MySQL database
 - database: the name of the database to connect to

The script assumes that the MySQL connector library and SQLAlchemy are
installed, and that the 'model_state' module is available.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def main():
    """
    Connect to the MySQL database, retrieve all state objects from it, and
    print their ID and name fields.
    """
    # Create a connection to the MySQL database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db),
        pool_pre_ping=True
    )

    # Create a session to the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Retrieve all state objects from the database and print their ID and name
    for instance in session.query(State).order_by(State.id):
        print("{:d}: {:s}".format(instance.id, instance.name))

    # Close the session to clean up resources
    session.close()

if __name__ == "__main__":
    main()
