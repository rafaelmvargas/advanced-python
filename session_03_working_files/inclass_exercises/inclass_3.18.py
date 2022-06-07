# 3.18:  BeautifulSoup object:  the below code reads a string
# read from an html file and parses the file and its tags into
# a BeautifulSoup object.

# Explore the following attributes of the object named 'soup':
#   * print the type of the object
#   * print the object itself
#   * print the .text attribute
# 

from bs4 import BeautifulSoup

scrapee = '../dormouse.html'

text = open(scrapee).read()
soup = BeautifulSoup(text, 'html.parser')


# Note that you may occasionally encounter a
# UnicodeDecodeError when you attempt to read a file from the
# internet.  In these cases you should tell Python which
# encoding to use:

text = open(scrapee, encoding='utf-8')

