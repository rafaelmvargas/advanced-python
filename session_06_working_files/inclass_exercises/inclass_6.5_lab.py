# 6.5:  Create a class Random that has a method get_rand(val)
# that returns a random number from 1 to the specified value.
# Call as shown.

# (A random number can be generated with random.randint(x, y)
# where x and y are the minimum and maximum values.)

import runreport

import random


class Random:
    def get_rand(self, val):
        return random.randint(1, val)


obj = Random()

val = obj.get_rand(5)  # random number from 1-5
print(val)

val2 = obj.get_rand(18)  # random number from 1-18
print(val2)

# Expected Output:

# 4
# 3
