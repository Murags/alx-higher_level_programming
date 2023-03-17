#!/usr/bin/python3
"""Module to connect to datbase"""
import MySQLdb
import sys


if __name__ == "__main__":
    user_name, password, db_name = sys.argv[1:]
    database = MySQLdb.connect(host='localhost', port=3306, user=user_name,
                           passwd=password, db=db_name, charset="utf8")
    curr = database.cursor()
    curr.execute('SELECT * FROM states ORDER BY id ASC')
    data = curr.fetchall()

    for state in data:
        print(state)

    curr.close()
    database.close()
