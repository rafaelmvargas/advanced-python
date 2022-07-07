"""
 solution_4.1.py -- Extract bytes downloaded by username
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/4/2022


"""

import re

sum_dict = {}
counter = 0

log_file = open("./access_log.txt", "r")

match_username = re.compile(r"/~([a-z]{1,4}\d+)")
match_bytes = re.compile(r"(\d+)$")

for line in log_file:
    nyu_id = re.search(match_username, line)
    file_size = re.search(match_bytes, line)

    if (nyu_id is not None) and (file_size is not None):

        counter += 1

        nyu_id = nyu_id.group(1)
        file_size = int(file_size.group(1))

        if nyu_id not in sum_dict:
            sum_dict[nyu_id] = 0
        sum_dict[nyu_id] += file_size

print(f"{counter} matches found (both user id and end-of-line bytes found on the line)")

for key in sorted(sum_dict, key=sum_dict.get, reverse=True):
    if sum_dict[key] > 10000000:
        print(f"{key}:  {sum_dict[key]}")
