# 7.7:  obj is an instance of the Do() class; an attribute has
# been set in the instance, and the class also has its own
# attribute, set as a class variable.  Investigate the
# instance and class attributes with the following tools:

#   1. regular attribute lookup (i.e., [instance].oattr and
# [instance].cval)
#   2. class lookup (i.e., [class].cval)
#   3. dir()
#   4. obj.__dict__
# 
# 

class Do():

    cval = 10

    def __init__(self):
        self.oattr = 500     # setting an attribute in the instance

    def dothis(self):
        print('done!')


obj = Do()

