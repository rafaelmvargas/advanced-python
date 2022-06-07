# 7.15:  Run the code to view the '.__doc__' attribute for the
# class and for the dothis() method.  Now add "docstrings"
# (floating triple-quoted strings) just inside both the class
# and def statements.  Run the program again to see how the
# .__doc__ attributes have changed.

class Do:

    d = 5

    def dothis(self):
        print('done!')


print(Do.__doc__)
print(Do.dothis.__doc__)

