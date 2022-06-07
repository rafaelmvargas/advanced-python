# 2.51:  Perform a loop within a loop within a complex
# structure.

# Using a loop nested within another 'for' loop, print each
# state, print and all 3 population values.  For clarity, try
# indenting each population value, and printing an extra blank
# line after each state.

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

# Indiana
#   6.7
#   6.5
#   6.1
# 
# Georgia
#   10.6
#   9.7
#   8.2
# 
# Alabama
#   4.9
#   4.8
#   4.4

