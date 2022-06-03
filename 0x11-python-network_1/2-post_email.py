#!/usr/bin/python3
"""Write a Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a
parameter, and displays the body of the response (decoded in utf-8)
"""

from sys import argv
import urllib.request
import urllib.parse

url_var = argv[1]
email = {'email': argv[2]}


email = urllib.parse.urlencode(email).encode('utf-8')

data = urllib.request.Request(url_var, email)
with urllib.request.urlopen(data) as response:
    print(response.read().decode('utf-8'))
