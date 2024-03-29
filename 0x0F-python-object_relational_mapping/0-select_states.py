#!/usr/bin/python3
''' lists all states from the database hbtn_0e_0_usa '''
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    connection = MySQLdb.connect(host='localhost', user=username,
                                 password=password,
                                 db=database, port=3306)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM states')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
