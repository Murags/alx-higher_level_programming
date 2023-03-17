#!/usr/bin/python3
"""Module to connect to database"""
import MySQLdb
from sys import argv


def main():
    """Print database items"""
    database = MySQLdb.connect(host="localhost", port=3306,
                                    user=argv[1], passwd=argv[2], db=argv[3])
    curr = database.cursor()
    qry = 'SELECT * FROM states WHERE name = "{}" ORDER BY id ASC'.format(argv[4])
    curr.execute(qry)
    data = curr.fetchall()
    for state in data:
        print(state)


if __name__ == '__main__':
    main()
