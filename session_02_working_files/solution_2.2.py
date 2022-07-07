"""
 solution_2.2.py -- CREATE TABLE / DROP TABLE
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/18/2022
"""

import sqlite3

db_name = 'session_2.db'
table_name = 'weather_newyork'

conn = sqlite3.connect(db_name)
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS weather_newyork')
cursor.execute('CREATE TABLE weather_newyork (date TEXT, mean_temp INT, precip FLOAT, events TEXT)')
conn.commit()


conn.close()


