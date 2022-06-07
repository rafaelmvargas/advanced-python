# 8.61:  Using the joined student tables, check to see if any
# null values can be found in the 'course' column.

import pandas as pd

sgrades = pd.read_csv('../student_db_grades.csv', sep=':')
snames = pd.read_csv('../student_db_names.csv')

sj = pd.merge(sgrades, snames, on='id', how='outer')


