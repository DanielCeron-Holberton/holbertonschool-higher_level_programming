#!/usr/bin/python3 
""" Module Filter states by user input"""


import MySQLdb
from sys import argv



if len(argv) <= 4:
    print("Not enough args")
    quit()

db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

cur = db.cursor()

query = "SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC".format(argv[4])

cur.execute(query)

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
db.close()


if __name__ == "__main__":
    pass

