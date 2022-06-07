# 2.33:  Read a table description.

# After doing a select * query on the students table, use the
# cursor .description attribute to retrive a tuple of tuples
# with tables names:

# ( ('id', None, None, None, None, None, None),
#   ('address', None, None, None, None, None, None),
#   ('city', None, None, None, None, None, None),
#   ('state', None, None, None, None, None, None),
#   ('zip', None, None, None, None, None, None)     )

import runreport

import sqlite3

conn = sqlite3.connect('../session_2.db')
cursor = conn.cursor()

query = 'SELECT * FROM students LIMIT 1'


# Next, use a list comprehension to retrieve a list of names:

# Expected Output:

# ['id', 'address', 'city', 'state', 'zip']

