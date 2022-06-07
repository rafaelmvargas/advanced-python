# 3.9:  Retrieve and save an image.

# Use the below URL to retrieve an image from the internet,
# and save it locally to a filename of your choice (make sure
# it has a .jpg file extension so it is recognized properly by
# your image viewer).
# 
# The data must be read and written as binary data (i.e., not
# plaintext).  Therefore when writing, use 'wb' (write binary)
# instead of 'w'.

import runreport

import requests

url = 'https://cdn.vox-cdn.com/uploads/chorus_image/image/32167377/monty-python-3by2.0.jpg'


