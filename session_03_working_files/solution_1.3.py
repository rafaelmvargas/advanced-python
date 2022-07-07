"""
 solution_3.1.py -- Date from new article
 
 Author: Rafael Vargas (rmv235@stern.nyu.edu)
 Last Revised: 6/28/2022

Pylance in VS Code states I must define para_count before using it, otherwise, my code will not run and a "NameError: name 'para_count' is not defined" is raised; In another set of homework, you dissuaded me from doing so.

"""

import requests
import bs4

url = "https://www.washingtonpost.com/technology/2022/06/21/nasa-sls-moon-rocket-space-launch-system/"

response = requests.get(url)
html_text = response.text

soup = bs4.BeautifulSoup(html_text, "html.parser")


# the title (please find it in a <meta> tag)
title_meta = soup.find("meta", attrs={"property": "og:title"})
print(f'Title: {title_meta.get("content")}\n')


# the author name(s) (please find it in a <meta> tag)
author_name = soup.find("a", attrs={"data-qa": "author-name"})
print(f"Byline: {author_name.text}\n")


# the date (please find it in a <meta> tag, then reformat as desired)
publish_date = soup.find("meta", attrs={"property": "article:published_time"})
formatted_date = publish_date.get("content")[:10]
print(f"Date: {formatted_date}\n")


# the paragraphs of the article
paragraphs = soup.find_all("p", attrs={"data-qa": "drop-cap-letter"})


# para_count = 0

for paragraph in paragraphs:
    para_count += 1
    print(paragraph.text, "\n")

print(f"[ {para_count} text paragraphs total ]")
