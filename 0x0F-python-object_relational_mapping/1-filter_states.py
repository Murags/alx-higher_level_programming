#!/usr/bin/python3
"""module to list database items"""
import MySQLdb
from sys import argv


def main():
    """List database items"""
    database = MySQLdb.connect(host='localhost', port=3306,
                                    user=argv[1], passwd=argv[2], db=argv[3])
    curr = database.cursor()
    query = 'SELECT id, name FROM states WHERE name LIKE "N%" ORDER BY id'
    curr.execute(query)
    data = curr.fetchall()
    for state in data:
        print(state)
    curr.close()
    database.close()


if __name__ == '__main__':
    main()
