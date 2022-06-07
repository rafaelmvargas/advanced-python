# 2.23:  Result set:  .fetchmany().  Use the cursor object to
# .execute() a SELECT query for all columns in the revenue
# table.  Use .fetchmany(3) to retrieve just 3 rows, then use
# .fetchmany(4) again to retrieve the remaining 4 rows.  Close
# the database connection when done.

import sqlite3

db_filename = '../session_2.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()

c.execute('SELECT * FROM revenue')


