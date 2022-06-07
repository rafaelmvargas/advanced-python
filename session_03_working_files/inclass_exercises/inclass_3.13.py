# 3.13:  Upload a file to a server program.  Add the files=
# parameter to .post() to upload the below file.

# Note that the file has been opened with 'rb', which stands
# for 'read binary':  we are uploading encoded bytes.

import requests

# open file for reading without decoding (returns a bytestring)
file_bytes = open('../test_file.txt', 'rb')

file_dict = { 'file':  ('test_file.txt', file_bytes,
                        'text/plain') }

response = requests.post('https://davidbpython.com/cgi-bin/http_reflect')

print(response.text)

