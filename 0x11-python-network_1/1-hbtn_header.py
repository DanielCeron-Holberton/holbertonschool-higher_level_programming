#!/usr/bin/python3
"""Module that fetch an URL"""


import urllib.request
from sys import argv


request = urllib.request.Request(argv[1])
with urllib.request.urlopen(request) as response:
    print(response.headers.get('X-Request-Id'))
