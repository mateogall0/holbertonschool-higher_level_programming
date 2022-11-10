#!/usr/bin/python3
"""list all states"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) < 4:
        exit()
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    except:
        exit()

    c = db.cursor()
    s = 'SELECT * FROM states WHERE name LIKE "{}";'.format(sys.argv[4])
    c.execute(s)
    rows = c.fetchall()
    for row in rows:
        if row[1] == sys.argv[4]:
            print(row)
    c.close()
    db.close()
