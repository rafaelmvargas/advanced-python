# 2.24:  Result set:  .fetchall().  Use the cursor object to
# .execute() a SELECT query for all columns in the revenue
# table.  Use .fetchall() to retrieve all rows in the result
# set as a list of tuples.  Close the database connection when
# done.

import sqlite3

db_filename = "../session_2.db"

conn = sqlite3.connect(db_filename)

c = conn.cursor()

c.execute("SELECT * FROM revenue")


print([t[0] for t in c.description])
