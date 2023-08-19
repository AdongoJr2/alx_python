#!/usr/bin/python3
"""My module"""

import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]
    host = "localhost"

    db = MySQLdb.connect(host=host, user=username, passwd=password, db=db_name)
    cur = db.cursor()

    cur.execute(
        """SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON states.id = cities.state_id
        WHERE states.name = BINARY %s
        ORDER BY cities.id ASC
        """,
        (state_name,)
    )

    result = cur.fetchall()

    def result_formatter(results):
        for item in results:
            print(item, end=", ")
        print('')  # for new line

    # for row in result:
    #     state = row[2]
    #     print("{}".format(state), end=", ")
    # print("")
    
    res = map(result_formatter, result)
    
    print(res)

    cur.close()
    db.close()
