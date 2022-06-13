"""
 solution_1.6.py -- slecting and writing rows based on row value
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/12/2022
"""
import csv

input_file = "revenue.csv"
output_file = "revenue_ny.csv"

ifh = open(input_file)
reader = csv.reader(ifh)

ofh = open(output_file, "w")
writer = csv.writer(ofh)

in_headers = next(ifh).rstrip().split(",")
out_headers = in_headers
writer.writerow(out_headers)

for company in reader:
    if company[1] == "NY":
        writer.writerow(company)

ifh.close()
ofh.close()
