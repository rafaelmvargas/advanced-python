"""
 solution_1.4.py -- return lookup dictionary of tickers to company name
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/12/2022
"""
import csv


def get_lookup(filename):
    fh = open(filename)
    reader = csv.reader(fh)

    lookup_dict = dict()

    for fields in reader:
        ticket, co_name, city, state = fields
        lookup_dict[ticket] = co_name

    return lookup_dict


filename = "nyse-listed_csv_tiny.csv"

lkpd = get_lookup(filename)

print(lkpd)
