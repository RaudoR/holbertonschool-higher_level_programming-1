#!/usr/bin/python3
"""takes in an argument and displays all values in the states table
where name matches the argument safe from SQL injection
Args:
    mysql username: name of the user
    mysql password: password for database
    database name: name of the database
    name searched: state name to search
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states\
    WHERE name = %s\
    ORDER BY states.id ASC", (argv[4], ))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
