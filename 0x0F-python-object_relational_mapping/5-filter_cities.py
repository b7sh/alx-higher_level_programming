#!/usr/bin/python3
'''
'''

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database, match_arg = sys.argv[1:]
    connection = MySQLdb.connect(host='localhost', user=username,
                                 password=password,
                                 db=database, port=3306)
    cursor = connection.cursor()
    cursor.execute("""SELECT cities.name FROM cities INNER JOIN \
                    states ON states.id=cities.state_id \
                    WHERE states.name=%s""", (match_arg,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
