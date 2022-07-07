"""
 solution_4.2.py -- Extract and sort stock ticker symbols by daily percent change
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 7/7/2022


"""
import re

symbols = re.compile(r"[A-Z]+, [+-]\d*.\d+")

fh = open("./market_discussion.txt")
text = fh.read()

tickers = re.findall(symbols, text)
sorted_tickers = sorted(tickers)

for sym in sorted_tickers:
    print(sym)

fh.close()


print("\n# Extra credit")

symbols = re.compile(r"([A-Z]+), ([+-]\d*.\d+)%")

fh = open("./market_discussion.txt")
text = fh.read()

tickers = re.findall(symbols, text)

sortable_dict = {}

for sym, price in tickers:
    sortable_dict[sym] = float(price)

sorted_dict = sorted(sortable_dict.items(), key=lambda item: item[1], reverse=True)

for sym, pct_change in sorted_dict:
    print(f"{sym}, {pct_change}")
