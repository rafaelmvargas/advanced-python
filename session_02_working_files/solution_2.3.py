"""
 solution_2.3.py -- CSV to SQL
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/20/2022
"""

import csv
import sqlite3

db_name = 'session_2.db'
table_name = 'weather_newyork'
csv_file = 'weather_newyork.csv'

conn = sqlite3.connect(db_name)
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)')
conn.commit()

ifh = open(csv_file)
reader = csv.reader(ifh)

in_headers = next(ifh).rstrip().split(',')

date_column = in_headers.index("date")
mean_temp_column = in_headers.index("mean_temp")
precip_column = in_headers.index("precip")
events_column = in_headers.index("events")

insert = 'INSERT INTO weather_newyork VALUES (?, ?, ?, ?)'

#tup = ()

for day in reader:
    date_in = day[date_column]
    mean_temp_in = day[mean_temp_column]
    precip_in = day[precip_column]
    if precip_in == "T":
        precip_in= None
    events_in = day[events_column]

    tup = (date_in,mean_temp_in,precip_in,events_in)
    cursor.execute(insert, tup)

conn.commit()
ifh.close()
conn.close()