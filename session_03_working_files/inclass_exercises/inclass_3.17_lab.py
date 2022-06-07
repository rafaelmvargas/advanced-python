# 3.17:  Read and parse CSV data.

# Request the following data and retrieve as text.  Load the
# text as a csv.reader object, then read line-by-line and
# print out each parsed line.
# 
# (Hint:  to load the data into text into csv.reader, split
# the text using .splitlines() first, and pass this list to
# csv.reader().)

import runreport

import csv
import requests

url = 'http://davidbpython.com/advanced_python/supplementary/dated_file.csv'



