# 8.4:  Use dir() to explore the attributes of the pandas
# module and a DataFrame; use help() to see the help text on
# pd.read_csv()

import pandas as pd

dol = {  'a': [1, 2, 3],
         'b': [2.9, 3.5, 4.9],
         'c': ['yourstr', 'mystr', 'theirstr']  }

df = pd.DataFrame(dol, index=['x', 'y', 'z'])

