#!/usr/bin/python3
"""Write a Python script that takes in a letter
and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    url = "http://0.0.0.0:5000/search_user"
    if len(argv) >= 2:
        letter = argv[1]
    else:
        letter = ""

    try:
        response = requests.post(url, data={'q': letter})
        json = response.json()
        if json:
            print('[{}]: {}'.format(json.get('id'), json.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
