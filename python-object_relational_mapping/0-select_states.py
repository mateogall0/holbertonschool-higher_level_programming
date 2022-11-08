#!/usr/bin/python3
"""list all states"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit()
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY states.id")
    row = c.fetchone()
    for row in c:
        print(row)
    db.close()
