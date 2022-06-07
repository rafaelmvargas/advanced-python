
import csv
import sqlite3

conn = sqlite3.connect('test.db')
c = conn.cursor()

c.execute('DROP TABLE IF EXISTS weather_newyork')

c.execute("""CREATE TABLE weather_newyork 
             ( date DATETIME, mean_temp INT, 
               precip FLOAT, events TEXT ) """)
conn.commit()


fh = open('weather_newyork.csv')
reader = csv.reader(fh)

header = next(reader)
print(header)

query = 'INSERT INTO weather_newyork VALUES (?, ?, ?)'

#for row in reader:
#    c.execute(query, (row[
