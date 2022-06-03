#!/usr/bin/python3
"""Module that takes in a URL,
    sends a request to the URL"""


from sys import argv
import urllib.request

url_var = argv[1]

request = urllib.request.Request(url_var)
with urllib.request.urlopen(request) as response:
    print(response.headers.get('X-Request-Id'))
