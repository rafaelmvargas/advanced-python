# 2.32:  Use .fetchall() to retrieve all rows.

# Select all columns from the students table where state is
# equal to NJ.  Use .fetchall() to retreieve the rows.

import runreport

import sqlite3

conn = sqlite3.connect('../session_2.db')
cursor = conn.cursor()


# Expected Output:

# ('jb23', '115 Karas Dr.', 'Jersey City', 'NJ', '07127')
# ('jb29', '119 Xylon Dr.', 'Jersey Cit', 'NJ', '07127')

