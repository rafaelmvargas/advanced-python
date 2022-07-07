# 2.47:  Access item in a dict of dicts.

# In a single statement, print 1819.

from os import popen
import runreport

dod = {
    "Indiana": {"year": "1816", "pop": 6.7},
    "Georgia": {"year": "1788", "pop": 10.6},
    "Alabama": {"year": "1819", "pop": 4.9},
}


# print(dod['Alabama']['year'])

# Expected Output:

# 1819

# Q1 traversing
# Q2 looping

for state in dod:  # str
    inner_dict = dod[state]  # dict, {'year': '116}
    print(state, inner_dict["pop"])


# for state, info in dod.items():
#     print(state, info['pop'])
