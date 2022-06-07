# 1.37:  Place the entire "set of company names" code (except
# for the imports, which should be outside the function) into
# new function get_companies(filename) that takes a filename
# as argument and returns the set of company names.

import runreport

filename = '../ad_companies.csv'

names = get_companies(filename)

print(names)

# Expected Output:

# {'Alpha Corp.', "Mike's Ads", 'Omni Media', 'Jones Kraft', 'Addy Ads'}

# (Order of your set may be different.)

