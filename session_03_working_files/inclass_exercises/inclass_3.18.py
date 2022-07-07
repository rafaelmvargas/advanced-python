# 3.18:  BeautifulSoup object:  the below code reads a string
# read from an html file and parses the file and its tags into
# a BeautifulSoup object.

# Explore the following attributes of the object named 'soup':
#   * print the type of the object
#   * print the object itself
#   * print the .text attribute
#

import requests  # a module for having your script act as a browser (web client)
import bs4  # a module for parsing HTML

url = "https://forecast.weather.gov/product.php?site=NWS&issuedby=CTP&product=AFD"

response = requests.get(url)  # a 'response' object

html_text = response.text  # text of the web page downloaded

# passing the HTML page text to the bs4 parser
# returns a soup object
soup = bs4.BeautifulSoup(html_text, "html.parser")

link_tags = soup.find_all('meta')
print(type(link_tags))
print(len(link_tags))

for tag in link_tags:
    print(tag.get('name'))

first_a = soup.find("a")
print(first_a)

print(first_a.name)  # the name of the tag
print(first_a.get("href"))  # the valuefor the href paramenter
print(first_a.text)  # any text found between open and close tag

# looking for a specifc tag using the name and parameters(s)
title_meta = soup.find("meta", attrs={"name": "DC.title"})

print(f"title: {title_meta.get('content')}")

exit()
# Type is a tag
first_meta = soup.find("meta")
print(type(first_meta))

# treat like dictorionary using get
print(first_meta.get("content"))
print(first_meta["content"])


# Note that you may occasionally encounter a
# UnicodeDecodeError when you attempt to read a file from the
# internet.  In these cases you should tell Python which
# encoding to use:

# text = open(scrapee, encoding='utf-8')
