#!/usr/bin/python3
"""Lists cities of a state"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", 3306, sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()

    cur.execute("""
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (sys.argv[4],))

    rows = cur.fetchall()
    print(", ".join(city[0] for city in rows))

    cur.close()
    db.close()
    