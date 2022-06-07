# 7.6:  Do is a class object; the class has a cval attribute
# assigned as a class variable.  Investigate the class'
# attributes with the following tools:

#   1. regular attribute lookup (i.e., .cval)
#   2. dir()
#   3. Do.__dict__.keys()
# 
# 

class Do:

    cval = 5

    def dothis(self):
        print('done!')


