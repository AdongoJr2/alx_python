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
        "SELECT * from states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")

    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
