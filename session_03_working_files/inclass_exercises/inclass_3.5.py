# 3.5:  Saving an image, sound or zip file.  Issue the below
# web request, open a local file with 'wb' (meaning, "write as
# bytes") and write the unencoded text to the file.  (To
# access unencoded text, use response.content instead of
# reponse.text).

import requests

url = 'https://davidbpython.com/advanced_python/supplementary/python.png'   # a URL to an image

response = requests.get(url)


# Check the folder where this script or notebook is located;
# you should find the image file there.

