"""
 solution_6.1.py -- Create a class Square
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/23/2022


"""


class Square:
    def __init__(self):
        self.int_attr = 2

    def squareme(self):
        self.int_attr = self.int_attr**2
        return self.int_attr

    def getme(self):

        return self.int_attr
