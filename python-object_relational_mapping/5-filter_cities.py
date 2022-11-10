#!/usr/bin/python3
"""list all states"""

import sys
import MySQLdb

if __name__ == "__main__":
    try:
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=sys.argv[1],
                             passwd=sys.argv[2],
                             db=sys.argv[3])
    except Exception:
        print('Error')
        exit()

    c = db.cursor()
    c.execute("""SELECT cities.name \
              FROM cities \
              JOIN states ON cities.state_id = states.id \
              WHERE BINARY states.name = %s \
              ORDER BY cities.id""", (sys.argv[4],))
    rows = c.fetchall()
    print(', '.join([str(i[0]) for i in rows]))
    c.close()
    db.close()
