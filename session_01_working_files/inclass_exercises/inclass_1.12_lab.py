# 1.12:  Use a 'for' loop to sum up int/float values in a
# file.  Sum up the 'volume' values in the file ad_buys.csv.


import runreport

fname = "../ad_buys.csv"
fh = open(fname)
next(fh)

sum = 0

for line in fh:
    volume = line.rstrip().split(",")[3]
    volume = int(volume)
    sum += volume

print(sum)


# Expected Output:

# 150
