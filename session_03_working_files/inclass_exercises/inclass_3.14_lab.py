# 3.14:  Demo exercise:  issue request with headers,
# parameters and data.

# Please note below the approach for setting headers,
# parameters and data in a request, and note that each have
# been successfully sent to (and reflected back from) the
# server.

import runreport

import requests

# link to my reflection program
url = 'http://davidbpython.com/cgi-bin/http_reflect'

div_bar = '=' * 10


# headers, parameters and message data to be passed to request
# change to 'text/html' for an HTML response
header_dict =  { 'Accept': 'text/plain' }
param_dict =   { 'key1': 'val1', 'key2': 'val2' }
data_dict =    { 'text1': "We're all out of gouda." }


# a GET request (change to .post for a POST request)
response = requests.get(url, headers=header_dict,
                             params=param_dict,
                             data = data_dict)


# status of the response (OK, Not Found, etc.)
response_status = response.status_code

# headers sent by the server
response_headers = response.headers

# body sent by server
response_text = response.text


# outputting response elements (status, headers, body)

# response status
print(f'{div_bar} response status {div_bar}\n')
print(response_status)
print(); print()

# response headers
print(f'{div_bar} response headers {div_bar}\n')
for key in response_headers:
    print(f'{key}:  {response_headers[key]}\n')
print()

# response body
print(f'{div_bar} response body {div_bar}\n')
print(response_text)

