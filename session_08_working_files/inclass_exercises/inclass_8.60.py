# 8.60:  Reading the same files but setting the 'id' column to
# the indexes of each DataFrame, use df.join() (the same
# operation as pd.merge()) to perform the above joins.

import pandas as pd

sgrades = pd.read_csv('../student_db_grades.csv', sep=':', index_col='id')
snames = pd.read_csv('../student_db_names.csv', index_col='id')


print(sgrades)
print()
print(snames)
print()
print(snames.join(sgrades))