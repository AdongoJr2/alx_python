#!/usr/bin/python3
"""My module"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"

    db = MySQLdb.connect(host=host, user=username, passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute(
        """SELECT cities.id, cities.name, states.name  
        FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        ORDER BY cities.id ASC
        """
    )

    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
