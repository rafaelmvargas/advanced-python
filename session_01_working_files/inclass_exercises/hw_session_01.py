# Ex 1.2
# Look through a file and count lines
fname = "../pyku.txt"

with open(fname) as fh:
    line_count = 0

    for line in fh:
        line.rstrip
        print(line)
        line_count += 1

    print(line_count)
