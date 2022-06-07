# 6.11:  Demonstrate class attributes.

# In the class below, set a class variable cvar to value 1000.
# 
# Print the value of cvar in three places:  1) instance a
# (a.cvar); 2) instance b (b.cvar); 3) the class itself
# (Something.cvar)
# 
# Also print the .attr attribute from each of the two
# instances.

class Something:
    # your class variable here

    def __init__(self, xx):
        self.attr = xx

a = Something('hi')
b = Something('there')


# print cvar in 3 places here

# print .attr from each of the two instances here

# Expected Output:

# 1000
# 1000
# 1000
# hi
# there

