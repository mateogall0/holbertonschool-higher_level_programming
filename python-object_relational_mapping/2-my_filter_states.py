#!/usr/bin/python3
"""list all states"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit()
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    c = db.cursor()
    c.execute('SELECT * FROM states WHERE name = "{}" ORDER BY states.id'.format(sys.argv[4]))
    row = c.fetchone()
    print(row)
    db.close()
