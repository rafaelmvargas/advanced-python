# 6.15:  Update Counter with an .increment() method that
# increments the attribute value each time it is called.  Call
# .increment() twice, then print the value of .counterval
# through the instance.

import runreport


class Counter:
    def __init__(self, val):
        self.counterval = val

    def increment(self):
        self.counterval += 1

    # your code here


c = Counter(5)

c.increment()
c.increment()

print(c.counterval)  # 7

# Expected Output:

# 7
