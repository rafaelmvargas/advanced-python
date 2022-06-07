# 1.36:  Use the csv module to parse a file and write to a new
# file.  Open file ad_buys.csv for reading and pass to
# csv.reader(), and new file ad_buys_totals.csv for writing
# and pass to csv.writer() (when opening the file for writing,
# include the newline='' parameter argument to write newlines
# properly).  As you loop through the read file, multiply the
# volume value by the price rounded to two places and add a
# new column, total, writing all columns to the new file.
# Make sure to include the headers with the new column label.

import runreport




# Expected Output:

# # at the end the file should contain:
# 
# datetime,buyer_id,seller_id,volume,price,total
# 1/14/18 8:33,1,2,20,0.083,1.66
# 1/14/18 8:38,2,4,10,0.083,0.83
# 1/14/18 8:41,1,2,8,0.061,0.49
# 1/14/18 8:48,1,4,12,0.13,1.56
# 1/14/18 8:59,2,1,14,0.072,1.01
# 1/14/18 9:02,4,2,3,0.073,0.22
# 1/14/18 9:06,2,4,6,0.098,0.59
# 1/14/18 9:09,1,4,18,0.14,2.52
# 1/14/18 9:15,4,1,16,0.1,1.6
# 1/14/18 9:18,1,2,6,0.043,0.26
# 1/14/18 9:22,2,1,14,0.033,0.46
# 1/14/18 9:28,6,4,2,0.029,0.06
# 1/14/18 9:38,2,4,10,0.083,0.83
# 1/14/18 9:39,4,2,3,0.073,0.22
# 1/14/18 9:41,1,2,8,0.061,0.49

