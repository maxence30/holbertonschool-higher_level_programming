#!/usr/bin/python3
"""Lists cities with their states"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", 3306, sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()

    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
    