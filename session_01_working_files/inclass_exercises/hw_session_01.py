# Ex 1.2
# Look through a file and count lines
from email import header


fname = "../pyku.txt"

with open(fname) as fh:
    line_count = 0

    for line in fh:
        line.rstrip
        print(line)
        line_count += 1

    print(line_count)

# Ex 1.3
fname = "../revenue.csv"
fh = open(fname)
next(fh)

sum = 0

for line in fh:
    line = line.rstrip().split(",")
    price = float(line[2])

    sum += price
print(sum)

# Ex 1.4
fname = "../student_db.txt"

fh = open(fname)
headers = next(fh)

id_list = []

for line in fh:
    line = line.rstrip()
    items = line.split(":")
    id = items[0]
    id_list.append(id)
print(id_list)


# Ex 1.5
fname = "../revenue.csv"

fh = open(fname)
headers = next(fh)

states = set()

for line in fh:
    line = line.rstrip()
    items = line.split(",")
    state = items[1]

    states.add(state)
print(states)

# Ex 1.6
fh = open("../student_db.txt")
headers = next(fh)  # skip next (first) line in file

sstate_dict = {}

for line in fh:
    items = line.split(":")
    stu_id = items[0]
    state = items[3]

    sstate_dict[stu_id] = state

print(sstate_dict)

test_key = input("Enter userID to get their state: ")

if test_key in sstate_dict:
    print(sstate_dict[test_key])
