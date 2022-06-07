# 2.26:  INSERT query.  Use the cursor object to .execute() an
# INSERT query, inserting a name, state and cost value into
# the revenue table.  Use parameterized arguments (?) to
# perform the insertions without having to worry about
# enquoting or escaping values in the query.

# Make sure to call conn.commit() (where conn is the
# connection object) to see results.  Also remember to close
# the database connection when done.
# 
# After running, return to your SQLite3 session and perform a
# SELECT * query so you can see the new row.

import sqlite3

db_filename = '../session_2.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()

query = 'INSERT INTO revenue VALUES (?, ?, ?)'


# If you don't see the change, make sure you executed
# conn.commit() after executing the insert.

