#!/usr/bin/python3
"""Lists all states with a name starting with N"""


import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd = sys.argv[2], db = sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    s = c.fetchall()
    for i in s:
        print(i)
