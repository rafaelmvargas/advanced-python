# 2.35:  Loop through database results and write rows to CSV.

# Select all rows from the planets table and insert them into
# a new file ../planets.csv file that you open for writing and
# write row-by row using a csv.writer object.  (Make sure to
# include the newline='' argument when opening the file, and
# to close the write file at the end.)

import runreport

import sqlite3

conn = sqlite3.connect('../session_2.db')
cursor = conn.cursor()


# The resulting file should look like this:

# Mercury,0.33,58
# Venus,4.87,108
# Earth,5.98,150
# Mars,64.2,228

