# 2.30:  SELECT query from planets table.

# Select all columns and rows from the 'planets' table
# (created in the previous lab), then use 'for' to loop over
# and print each row of results.

import runreport

import sqlite3

conn = sqlite3.connect('../session_2.db')
cursor = conn.cursor()


# Expected Output:

# ('Mercury', '0.33', '58')
# ('Venus', '4.87', '108')
# ('Earth', '5.98', '150')

