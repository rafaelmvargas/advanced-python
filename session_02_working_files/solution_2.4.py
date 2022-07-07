"""
 solution_2.4.py -- JSON to SQL
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/20/2022
"""

import json
import sqlite3


db_name = 'session_2.db'
json_file = 'weather_newyork_dod.json'

conn = sqlite3.connect(db_name)

cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)')

conn.commit()

ifh = open(json_file)
reader = json.load(ifh)

insert = 'INSERT INTO weather_newyork VALUES (?, ?, ?, ?)'

tup = ()

for day in reader:
    inner_dict = reader[day]

    date = day
    mean_temp = inner_dict['mean_temp']
    precip = inner_dict['precip']
    if precip=='T':
        precip=None
    events = inner_dict['events']

    tup = (date, mean_temp,precip, events)
    cursor.execute(insert, tup)

conn.commit()
ifh.close()
conn.close()