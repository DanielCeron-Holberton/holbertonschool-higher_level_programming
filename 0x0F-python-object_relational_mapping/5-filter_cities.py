#!/usr/bin/python3
""" Module that filter cities"""

import MySQLdb
from sys import argv

if len(argv) <= 4:
    print("Not enough args")
    quit()

conn = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

cur = conn.cursor()

cur.execute("""SELECT cities.name
               FROM cities
               JOIN states
               ON states.id = cities.state_id
               WHERE states.name = %s
               ORDER BY cities.id ASC;""", (argv[4], ))

rows = cur.fetchall()

for row in rows:
    if row is not rows[-1]:
        print(row[0], end=', ')
    else:
        print(row[0])

cur.close()
conn.close()
