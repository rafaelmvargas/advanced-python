"""
 solution_6.2.py -- Create a class that list of a Maximum Size
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/23/2022


"""


class MaxSizeList:
    """
    Class to create a list with a  maximum number items
    """

    def __init__(self, max_size: int):
        self.list = []
        self.max_size = max_size

    def push(self, text: str):
        """
        Add items to list and check if size is at maximum, if it is, remove first item
        """
        if len(self.list) == self.max_size:
            self.list.pop(0)
        self.list.append(text)

    def get_list(self):
        """
        Return list of limited items
        """
        return self.list
