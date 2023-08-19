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

    sql_query = "SELECT * from states WHERE name LIKE BINARY 'N%' ORDER BY id ASC"
    cur.execute(sql_query)

    result = cur.fetchall()

    for row in result:
        print(row)

    cur.close()
    db.close()
