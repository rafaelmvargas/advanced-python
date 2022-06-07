# 7.8:  class What inherits from class Do.  Investigate the
# What instance attributes with the following tools:

#   1. regular attribute lookup (i.e., .cval)
#   2. dir()
#   3. Do.__dict__.keys()
# 

class Do:

    dovar = 5

    def dothis(self):
        print('done!')


class What(Do):

    whatvar = 10

    def __init__(self):
        self.instval = 500

z = What()

