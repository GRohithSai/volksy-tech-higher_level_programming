#!/usr/bin/python3


def getAllstates(user2, password2, db2):
    """Script that gets all the states when called on"""
    import MySQLdb
    conn = MySQLdb.connect(host="localhost", port=3306, user=user2,passwd=password2, db=db2, charset="utf-8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
if __name__ == "__main__":
    import sys
    """ protected from executing when imported"""
    getAllstates(sys.argv[1], sys.argv[2], sys.argv[3])
