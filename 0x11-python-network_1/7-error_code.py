#!/usr/bin/python3
"""Write a Python script that takes in a URL,
sends a request to the URL and displays
the body of the response.
"""

if __name__ == "__main__":
    import requests
    from requests.exceptions import HTTPError
    from sys import argv

    url = argv[1]
    response = requests.get(url)
    if (response.status_code < 400):
        print(response.text)
    else:
        print('Error code: {}'.format(response.status_code))
