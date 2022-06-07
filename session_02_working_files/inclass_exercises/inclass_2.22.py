# 2.22:  Result set:  .fetchone().  Use the cursor object to
# .execute() a SELECT query for all columns in the revenue
# table WHERE company = 'Westfield', and use .fetchone() to
# retrieve the single result row (tuple) of values.  Close the
# database connection when done.

import sqlite3

db_filename = '../session_2.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()

c.execute("SELECT * FROM revenue WHERE company = 'Westfield'")


