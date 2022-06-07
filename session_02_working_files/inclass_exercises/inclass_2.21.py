# 2.21:  Result set:  for looping.  Use the cursor object to
# .execute() a SELECT query for all columns in the revenue
# table, and loop through the result set object with a for
# loop, printing each row.  Close the database connection when
# done.

import sqlite3

db_filename = '../session_2.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()

