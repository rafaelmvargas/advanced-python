# 1.4:  Loop through a file, split out a column and append to
# a list.  Before the loop begins, initialize an empty list.
# Perform the same operations as in previous, but add each id
# value (the first field value in each line) to the list.

fname = '../student_db.txt'

fh = open(fname)
headers = next(fh)             # retrieve next (first) line from file

for line in fh:
    line = line.rstrip()
    items = line.split(':')



