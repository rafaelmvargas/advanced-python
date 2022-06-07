# 6.7:  Demonstration:  note the unique identifier of self and
# an instance from a class.

# At the bottom of the code below, print obj, then call
# obj.something(), noting that this method prints self.
# Compare the hex codes that identify the instance.
# 
# Use a print() statement to create a blank line.
# 
# Next, print obj2 and call obj2.something(), and note the
# output, particularly the hex codes.

class Do:
    def something(self):
        print(self)


obj = Do()
obj2 = Do()

# your code here

# Expected Output:

# <__main__.Do object at 0x10d648350>
# <__main__.Do object at 0x10d648350>
# 
# <__main__.Do object at 0x10d648390>
# <__main__.Do object at 0x10d648390>

