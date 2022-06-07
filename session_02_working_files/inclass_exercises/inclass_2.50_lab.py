# 2.50:  Loop through and print 'column' values in a complex
# structure.

# Using a loop, print the values 1816, 1788 and 1819 from the
# below structure:

import runreport

struct = { 'version':  1.1,
           'data': {
                'states': {
                    'Indiana':  {
                                   'year': '1816',
                                   'pop':  [ 6.7, 6.5, 6.1 ]
                                },
                    'Georgia':  {
                                   'year': '1788',
                                   'pop':  [ 10.6, 9.7, 8.2 ]
                                },
                    'Alabama':  {
                                   'year': '1819',
                                   'pop':  [ 4.9, 4.8, 4.4 ]
                                }
                },
                'pop_years':  [ '2019', '2010', '2000']
            }
        }

# Expected Output:

# 1816
# 1788
# 1819

