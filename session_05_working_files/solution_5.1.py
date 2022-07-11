"""
 solution_5.1.py -- Sort by canonical date
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/10/2022


"""
from datetime import datetime


source_fname = "dated_file.csv"
target_fname = "sorted_file.csv"


def line_by_date(this_line):
    """this sorting helper function takes a single line as argument
    and returns the value by which that line should be sorted"""

    date_str = this_line.split(",")[0]

    new_string = date_str[6:] + date_str[0: 2] + date_str[3: 5]

    return new_string


# read the file into a list of lines
fh = open(source_fname)
lines = fh.readlines()


slines = sorted(lines, key=line_by_date)


# write the lines to a new file
wfh = open(target_fname, "w")  # open file for writing
for line in slines:
    wfh.write(line)
wfh.close()

print(f"wrote to {target_fname}")
