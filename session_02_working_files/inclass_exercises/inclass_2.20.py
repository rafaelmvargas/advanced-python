# 2.20:  Database connect and cursor().  In a Python program,
# connect to ../session_2.db (returning a connection object)
# and call .cursor() on it to get a cursor object we will use
# for querying.  (Note the ../ assumes that we are in a
# directory above the session_2.db file.)

# Close the database connection with conn.close() when
# finished.

import sqlite3

db_filename = '../session_2.db'


