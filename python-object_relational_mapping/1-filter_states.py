#!/usr/bin/python3
""""It displays all the records with given condtion"""


import sys
importMySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id")
    for i in c:
        if i[1][0] == "N":
            print(i)
