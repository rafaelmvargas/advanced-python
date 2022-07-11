"""
 solution_5.3.py -- Sort the keys in a dict of dicts by each dict's mean_temp, then prints each key and associated dict
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/10/2022


"""
import json


def by_mean_temp(arg):
    return int(dod[arg]["mean_temp"])


fh = open("weny_dod_tiny.json")
dod = json.load(fh)

keys = sorted(dod, key=by_mean_temp)

for key in keys:
    print(f"{key}:  {dod[key]}")
