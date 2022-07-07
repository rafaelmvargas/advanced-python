# 2.20:  Database connect and cursor().  In a Python program,
# connect to ../session_2.db (returning a connection object)
# and call .cursor() on it to get a cursor object we will use
# for querying.  (Note the ../ assumes that we are in a
# directory above the session_2.db file.)

# Close the database connection with conn.close() when
# finished.

import sqlite3  # import pymysql import oracle_cx

db_filename = "../session_2.db"


conn = sqlite3.connect(db_filename)  # a db connection object
cursor = conn.cursor()  # a cursor object
cursor.execute("SELECT * FROM revenue")

# one row: .fetchone()
# row = cursor.fetchone()
# print(row)


# multiple rows: .fetchmany(n)
# rows = cursor.fetchmany(3)

# all rows: .fetchall()
# rows = cursor.fetchall()
# print(rows)

#'for' looping over result set rows
# for row in cursor:
#     print(row)

conn.close()
