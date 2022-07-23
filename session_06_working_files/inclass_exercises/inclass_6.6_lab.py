# 6.6:  Create a class Math with method add() that takes two
# integer arguments and returns the values summed.

import runreport


class Math:
    def add(self, intx, inty):
        return intx + inty


obj = Math()

mysum = obj.add(5, 10)  # 15
print(mysum)

mysum2 = obj.add(100, 150)  # 250
print(mysum2)

# Expected Output:

# 15
# 250
