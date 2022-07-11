"""
 solution_5.2.py -- Sort a list of dicts by each dict's mean_temp
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/10/2022


"""
import json


def by_mean_temp(arg):
    return int(arg["mean_temp"])


fh = open("weny_lod_tiny.json")
lod = json.load(fh)

sorted_dicts = sorted(lod, key=by_mean_temp)

for idict in sorted_dicts:
    print(idict)
