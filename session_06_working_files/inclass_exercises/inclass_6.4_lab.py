# 6.4:  Create a class Time that has a method get_time() that
# returns the current time.  Call as shown.

# (A string showing the current time can be obtained from the
# time module using time.ctime().)

import runreport

import time


class Time:
    def get_time(self):
        return time.ctime()


obj = Time()
print(obj.get_time())  # should show the current time

# Expected Output:

# Sat Oct 17 18:41:34 2020    (as your specific date and time)
