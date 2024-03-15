#!/usr/bin/python3
''' lists all cities from the database hbtn_0e_4_usa '''

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    connection = MySQLdb.connect(host='localhost', user=username,
                                 password=password,
                                 db=database, port=3306)
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM \
                    cities INNER JOIN states ON states.id=cities.state_id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
