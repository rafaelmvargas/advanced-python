"""
 solution_7.1.py -- Load and save config to file via a class
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/23/2022


"""
import csv

class Config:
    def __init__(self, fname: str):
        self.fname = fname

        fh = open(fname, "r")
        config_file = csv.reader(fh)

        for line in config_file:
            configs = line
            print(configs)

        fh.close()


test = Config("pconfig copy.csv")
