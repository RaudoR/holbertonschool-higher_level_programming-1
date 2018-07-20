#!/usr/bin/python3
"""script that lists all states with a name starting with N
Args:
    mysql username: name of the user
    mysql password: password for database
    database name: name of the database
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
    WHERE name LIKE 'N%'\
    ORDER BY states.id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
