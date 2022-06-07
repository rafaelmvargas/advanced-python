# 2.28:  Write several rows to csv.  Open the file new2.csv
# for writing and use writer.writerow() to write the header,
# followed by using writer.writerows() to write the entire
# list of tuples, to the file.  Make sure to close the file
# after writing.

import csv

header = ['name', 'state', 'country']
rows = [ ('Joe', 'CA', 'USA'),
         ('Mary' ,'NY', 'USA') ]

wfh = open('../new2.csv', 'w', newline='')
writer = csv.writer(wfh)


