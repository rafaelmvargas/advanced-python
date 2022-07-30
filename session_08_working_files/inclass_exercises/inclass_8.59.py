# 8.59:  View the two below DataFrames.  Then use pd.merge()
# to join the student_db_grades.csv and student_db_names.csv
# files into a single DataFrame, joining on the id (use
# on='id').  Compare "how='outer'" (19 rows, including missing
# data at the end) to "how='inner'" (only 15 rows, with ids
# common to both tables) to effect an outer join.

import pandas as pd

sgrades = pd.read_csv("../student_db_grades.csv", sep=":")
snames = pd.read_csv("../student_db_names.csv")


# print(sgrades)
# print()


snames = snames.set_index('id')
print(snames)
snames =snames.reset_index()
print(snames)
print(pd.merge(snames, sgrades, on="id"))
