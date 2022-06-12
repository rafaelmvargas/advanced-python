"""
 solution_1.3.py -- return sorted list of unique words
 
 Author: Rafael Vargas (rmv235@nyu.edu)
 Last Revised: 6/12/2022
"""


def collect_unique(filename):
    list_of_words = []
    set_of_words = set()

    fh = open(filename)

    text = fh.read().lower().split()

    for word in text:
        word = word.strip(",.;")
        set_of_words.add(word)

    list_of_words = sorted(list(set_of_words))

    return list_of_words


filename = "sonnet_xv_tiny.txt"

words = collect_unique(filename)

print(words)
