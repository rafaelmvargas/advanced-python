"""
 solution_1.5.py -- make a narrower weather new york file
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/12/2022
"""
import csv


input_file = "weather_newyork_tiny.csv"
output_file = "weather_newyork_narrow.csv"

ifh = open(input_file)
reader = csv.reader(ifh)

ofh = open(output_file, "w")
writer = csv.writer(ofh)

in_headers = next(ifh).split(",")
date_column = in_headers.index("date")
mean_temp_column = in_headers.index("mean_temp")
precip_column = in_headers.index("precip")
events_column = in_headers.index("events")

select_headers = ["date", "mean_temp", "precip", "events"]

writer.writerow(select_headers)

for day in reader:

    date_in = day[date_column]
    mean_temp_in = day[mean_temp_column]
    precip_in = day[precip_column]
    events_in = day[events_column]
    writer.writerow([date_in, mean_temp_in, precip_in, events_in])

ifh.close()
ofh.close()
