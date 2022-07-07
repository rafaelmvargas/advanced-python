"""
 solution_2.1.py -- SQL to CSV
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/18/2022
"""

import sqlite3
import csv

db_name = 'session_2.db'
table_name = 'revenue'
csv_filename = 'revenue_from_db.csv'


def sql_to_csv(db_name, table_name, csv_filename):
   conn = sqlite3.connect(db_name)
   cursor = conn.cursor()
   cursor.execute(f'SELECT * FROM {table_name}')
   db_result = cursor.fetchall()
   
   fh = open(csv_filename,"w")
   writer = csv.writer(fh)

   write_headers = [x[0] for x in cursor.description]
   writer.writerow(write_headers)

   for company_stats in db_result:
      writer.writerow(company_stats)

   fh.close()
   conn.close()


sql_to_csv(db_name,table_name, csv_filename)


