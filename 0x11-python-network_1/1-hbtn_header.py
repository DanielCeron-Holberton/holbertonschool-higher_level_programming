#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL
and displays the value of the X-Request-Id Header
in the console
"""


import urllib.request
from sys import argv

url_var = argv[1]

request = urllib.request.Request(url_var)
with urllib.request.urlopen(request) as response:
    print(response.headers.get('X-Request-Id'))
