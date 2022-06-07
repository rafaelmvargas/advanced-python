# 1.5:  Loop through a file, split out a column and add to a
# set.  Similar to previous, use a set to collect a unique
# collection of states found in revenue.csv

fname = '../revenue.csv'

fh = open(fname)

for line in fh:
    line = line.rstrip()
    items = line.split(',')



