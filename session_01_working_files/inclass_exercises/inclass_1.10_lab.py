# 1.10:  Use a 'for' loop to print selected lines.  Loop
# through ad_companies.csv and print out only those lines with
# a state of AZ.

import runreport

fname = "../ad_companies.csv"

fh = open(fname)
next(fh)

for line in fh:
    id, company, city, state = line.rstrip().split(",")
    if state == "AZ":
        print(line.rstrip())


# Expected Output:

# 3,Omni Media,Phoenix,AZ
# 5,Addy Ads,Tempe,AZ

# Please note that there is no blank line printed after each
# line.
