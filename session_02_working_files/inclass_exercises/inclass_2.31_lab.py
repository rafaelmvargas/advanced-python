# 2.31:  Use .fetchone() to retrieve one row.

# Select all columns from the user table where user_id is
# equal to 2.  Use .fetchone() to retreieve the row.

import runreport

import sqlite3

conn = sqlite3.connect('../session_2.db')
cursor = conn.cursor()


# Expected Output:

# (2, 'joe', 'pass', 'Joe', 'Wilson')

