#!/usr/bin/python3
"""List Module"""


import MySQLdb
from sys import argv


if len(argv) <= 3:
    print("Not enough args")
    quit()


db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

cur = db.cursor()

cur.execute("SELECT * FROM first_table ORDER BY id ASC")

rows = cur.fetchall()

for row in rows:
    print(row)
