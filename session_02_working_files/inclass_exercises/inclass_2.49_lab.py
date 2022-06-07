# 2.49:  Access an item in a complex structure.

# Print the value 9.7 in the below structure:

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

# 9.7

