"""
 solution_1.1.py -- sum price where buyer_id is one
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/12/2022
"""

fname = "ad_buys.csv"

fh = open(fname)

next(fh)

sum = float()

for line in fh:
    datetime, buyer_id, seller_id, volume, price = line.rstrip().split(",")

    if buyer_id == "1":
        print(price)
        sum += float(price)

print(f"\nsum: {sum}")
