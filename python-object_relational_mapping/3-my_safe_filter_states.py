#!/usr/bin/python3
"""Safe filter states"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", 3306, sys.argv[1], sys.argv[2], sys.argv[3])
    cur = db.cursor()

    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
