# 3.4:  Issue a web request, view response.text (decoded) and
# response.content (undecoded).

# With the first URL, check the type of response.text and the
# type of response.content.  Each contains the response
# content, but one is decoded as a string and the other is
# encoded as bytes.
# 
# Next, check the value of response.encoding to see what
# encoding the yahoo page uses.  The check the same with the
# Microsoft English page and the Microsoft French page.

import requests

url = 'http://www.yahoo.com'

# url = 'https://www.microsoft.com/en-us/'      # Microsoft in English
# url = 'https://www.microsoft.com/fr-fr/'      # Microsoft in French

response = requests.get(url)



