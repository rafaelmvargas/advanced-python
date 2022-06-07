# 8.21:  Read a DataFrame from sqlite_sample.db using a
# database connection and the below query.

import pandas as pd
import sqlite3

conn = sqlite3.connect('../sqlite_sample.db')

query = 'SELECT * FROM planets'

