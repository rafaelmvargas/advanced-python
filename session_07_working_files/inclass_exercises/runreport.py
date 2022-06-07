""" 
    runreport.py -- send contents of executing code to instructor's CGI 
    Author:      David Blaikie (david@davidbpython.com)
    Version:     0.1.1
    Last revised:  2020-09-20
"""



import os
import re
import sys
import subprocess
import urllib
from urllib import request
from urllib.parse import urlencode, quote_plus
from multiprocessing import Process


MODNAME = 'runreport.py'
REMOTE_URL = 'http://davidbpython.com/cgi-bin/runreport_log.cgi'


def send(name, text):
    """ send the user's name and script text """

    payload = {  'username': name,
                 'filename': this_filename,
                 'code':     text  }

    query_string = urlencode(payload, quote_via=quote_plus)

    request.urlopen(REMOTE_URL + '?' + query_string)



def name(this_name='', script_name=None):
    """ function called by the user to send script text 
        script_name may be used later 
        (if we can incorporate with notebook) """

    # original version used this standin text - ignore
    if 'please replace' in this_name:
        return

    # if name in username.txt is empty or spaces
    if not this_name or re.search(r'^\s+$', this_name):
        print('runreport.py:  save your name in "username.txt" (in this directory), ')
        print('               or comment out "import runreport" in your script ')
        print('               to suppress this message.')
        print()
        return

    this_name = this_name.replace(' ', '_')
    this_name = re.sub(r'[^a-zA-Z_]', '', this_name)

    try:
        text = open(sys.argv[0]).read()
        send(this_name, text)
    except Exception as e:
        print('exception: ' + str(e))



this_filename = os.path.basename(sys.argv[0])
try:
    username = ( open('../../username.txt').read()
                 .lower().strip().strip("'\"[]()")
                 .replace('\n', '').replace('\r', '').replace('\t', '')
               ) 
except FileNotFoundError:
    username = ''


# reject Python 2
if sys.version_info[0] != 3:
    raise ValueError(f'{MODNAME} is usable only with Python 3')


# reject notebook execution
import __main__
if not hasattr(__main__, '__file__'):
    raise ImportError(f'{MODNAME} cannot be imported from the interactive Python interpreter')


name(username)




