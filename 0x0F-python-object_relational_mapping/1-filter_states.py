#!/usr/bin/python3
"""Module list with filter"""

import MySQLdb
from sys import argv


if len(argv) <= 3:
    print("Not enough args")
    quit()


db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

cur = db.cursor()

cur.execute("SELECT * FROM states ORDER BY id ASC")

rows = cur.fetchall()

for row in rows:
    if row[1][0] == "N":
        print(row)

if __name__ == "__main__":
    pass
