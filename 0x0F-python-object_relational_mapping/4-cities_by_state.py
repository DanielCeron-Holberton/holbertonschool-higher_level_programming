#!/usr/bin/python3
""" Module that filter cities"""

import MySQLdb
from sys import argv

if len(argv) <= 3:
    print("Not enough args")
    quit()

conn = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])

cur = conn.cursor()

cur.execute("""SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states
            ON cities.state_id=states.id
            ORDER BY cities.id ASC""")

rows = cur.fetchall()

for row in rows:
    print(row)

cur.close()
conn.close()
