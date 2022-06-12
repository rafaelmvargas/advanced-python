"""
 solution_1.2.py -- return mean list of integer temperatures
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/12/2022
"""


from math import ceil
from statistics import stdev


def collect_mean_temps(filename):

    mean_temperatures = []

    fh = open(filename)
    next(fh)

    for day in fh:
        mean_temp = day.rstrip().split(",")[1]
        mean_temperatures.append(int(mean_temp))

    return mean_temperatures


filename = "weather_newyork_tiny.csv"
meantemps = collect_mean_temps(filename)
print(meantemps)

length = int(len(meantemps))
average = sum(meantemps) / length
print(average)

sorted_meantemps = sorted(meantemps)

if length % 2 == 0:
    left = int(length / 2 - 1)
    right = int((length / 2))
    median = (sorted_meantemps[left] + sorted_meantemps[right]) / 2
else:
    middle = ceil(length / 2 - 1)
    median = sorted_meantemps[middle]

print(median)
print(stdev(meantemps))


#####
def collect_file_values(filename, column):

    mean_values = []

    fh = open(filename)

    headers = next(fh).rstrip().split(",")
    read_column = headers.index(column)

    for day in fh:
        data = day.rstrip().split(",")[read_column]
        mean_values.append(int(data))

    return mean_values


filename = "weather_newyork_tiny.csv"

values = collect_file_values(filename, "mean_visibility")

print(values)
