# 6.14:  Create class Counter, initialized with an integer as
# shown below.  Set the attribute .counterval in __init__ so
# that it is available in the instance.

import runreport


class Counter:
    def __init__(self, counterval=0):
        self.counterval = counterval


c = Counter(5)

print(c.counterval)  # 5

# Expected Output:

# 5
