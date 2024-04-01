#!/usr/bin/python3
"""
    takes in a URL, sends a request
    to the URL and displays the body
    of the response.
"""


if __name__ == "__main__":
    import requests
    import sys

    req = sys.argv[1]
    r = requests.get(req)
    if r.status_code >= 400:
        print("Error code:".format(r.status_code))
    else:
        print(r.text)
