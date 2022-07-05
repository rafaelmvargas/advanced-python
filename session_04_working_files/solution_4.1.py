"""
 solution_4.1.py -- Extract bytes downloaded by username
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/4/2022


"""

import re

sum_dict = {}
counter = 0

log_file = open("./access_log.txt", "r")

for line in log_file:
    match_username = re.search(r"/~([a-z]{1,4}\d+)", line)
    match_bytes = re.search(r"(\d+)$", line)

    if match_username and match_bytes is not None:
        counter += 1
        # print(match_username.group(1), match_bytes.group(1))
        nyu_id = match_username.group(1)
        file_size = int(match_bytes.group(1))
        if nyu_id not in sum_dict:
            sum_dict[nyu_id] = 0
        sum_dict[nyu_id] += file_size

print(f"{counter} matches found (both user id and end-of-line bytes found on the line)")

for key in sorted(sum_dict, key=sum_dict.get, reverse=True):
    if sum_dict[key] > 10000000:
        print(f"{key}:  {sum_dict[key]}")
