#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main_"_:
    connection = MySQLdb.connect(host='localhost', user=sys.argv[1],
                                 password=sys.argv[2],
                                 db=sys.argv[3], port=3306)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM states')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
