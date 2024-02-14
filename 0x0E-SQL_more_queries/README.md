This is the readme file for the 0x0E. SQL - More queries project.

General:

- How to create a new MySQL user.
- How to manage privileges for a user to a database or table.
- What’s a PRIMARY KEY.
- What’s a FOREIGN KEY.
- How to use NOT NULL and UNIQUE constraints.
- How to retrieve datas from multiple tables in one request.
- What are subqueries.
- What are JOIN and UNION.

Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$

This is the mandatory tasks:

0. My privileges!
1. Root user
2. Read user
3. Always a name
4. ID can't be null
5. Unique ID
6. States table
7. Cities table
8. Cities of California
9. Cities by States
10. Genre ID by show
11. Genre ID for all shows
12. No genre
13. Number of shows by genre
14. My genres
15. Only Comedy
16. List shows and genres

Thia ia the advanced tasks:

17. Not my genre
18. No Comedy tonight!
19. Rotten tomatoes
20. Best genre
