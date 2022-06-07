# 8.30:  First, view the below DataFrame.  Note the
# index_col='id' parameter set the index to the 'id' column.
# Next, use .reset_index() to reset the index to the default
# (integers), while moving the index to a new column.  Lastly,
# add the drop=True parameter argument to drop the index
# entirely, and note that the old index has been dropped.

import pandas as pd

df = pd.read_csv('../student_db_names.csv', index_col='id')


