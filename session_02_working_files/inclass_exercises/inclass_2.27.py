# 2.27:  Write a row to a csv.  Open a new file new.csv for
# writing (remember that this will truncate (blank out) the
# file).  Using write.writerow(), write the header row first,
# then the data in row and row2 to the file.  Make sure to
# close the file before finishing (especially in Jupyter,
# where the program does not stop running and so the file will
# not be closed until you close the notebook).  To confirm,
# open the file directly in a text editor or Excel to view it.

import csv

header = ['name', 'state', 'country']
row = ['Joe', 'CA', 'USA']
row2 = ['Mary', 'NY', 'USA']

wfh = open('../new.csv', 'w', newline='')
writer = csv.writer(wfh)


