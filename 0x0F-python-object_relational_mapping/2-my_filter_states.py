#!/usr/bin/python3
'''
    takes in an argument and displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument.
'''
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, match_arg = sys.argv[1:]
    connection = MySQLdb.connect(host='localhost', user=username,
                                 password=password,
                                 db=database, port=3306)
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states \
                    WHERE name LIKE BINARY '{}'".format(match_arg))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
