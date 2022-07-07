# 4.22:  Match on files with date format YYYY-MM-DD followed
# by '.txt'.

import runreport

import re

dirlist = ('.', '..', '2010-12-15.txt', '2010-12-16.txt',
           'testfile.txt', '20101-11-03.txt')

for item in dirlist:
    if re.search(r'^[\d]{4}-[\d]{2}-[\d]{2}\.txt', item):
        print(item)

# Expected Output:

# 2010-12-15.txt
# 2010-12-16.txt

