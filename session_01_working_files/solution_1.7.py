"""
 solution_1.7.py -- Dict aggregation, reverse sort for values more than one
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/12/2022
"""
import string

fname = "sonnet_xv.txt"

fh = open(fname)

word_count = dict()

text = fh.read().lower().split()

for word in text:
    word = word.strip(string.punctuation)
    if word not in word_count:
        word_count[word] = 1
    else:
        word_count[word] += 1


assert word_count["in"] == 5
assert word_count["new"] == 1

new_dict = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
for word, count in new_dict:
    if count > 1:
        print(f"{word}:  {count}")
