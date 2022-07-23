# 6.17:  Set a class variable, 'increment_value' to 3 - this
# will specify how much the increment() method should increase
# the attribute.  Add this value to the .counterval attribute
# in increment().

import runreport


class Counter:
    increment_value = 3

    def __init__(self, val):
        self.counterval = val

    def increment(self):
        self.counterval += Counter.increment_value


c = Counter(5)

c.increment()
c.increment()

print(c.counterval)  # 11 (5 + 3 + 3)

# Expected Output:

# 7
