# 2.34:  Insert a row.

# Insert a new row into the planets table with the following
# data:

# Mars    64.20    228

import runreport

import sqlite3

conn = sqlite3.connect('../session_2.db')
cursor = conn.cursor()


# After committing the insert with conn.commit(), issue a
# SELECT query to confirm that the row has been inserted.

import runreport



