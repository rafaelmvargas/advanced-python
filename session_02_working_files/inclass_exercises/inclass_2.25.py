# 2.25:  Show table columns.  After doing a select * query,
# use the cursor .description attribute to see the names of
# columns in a table, which are nested in a list of tuples.
# Then pull out just the first item in each tuple to get a
# list of columns.  Close the database connection when done.

import sqlite3

db_filename = '../session_2.db'

conn = sqlite3.connect(db_filename)

c = conn.cursor()

c.execute('SELECT * FROM revenue LIMIT 1')


# We're using a LIMIT 1 to pull just one row from the table,
# which will have all columns.

