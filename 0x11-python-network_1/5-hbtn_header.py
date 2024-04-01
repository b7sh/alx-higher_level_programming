#!/usr/bin/python3
"""
    takes in a URL, sends a request to the URL
    and displays the value of the variable
    X-Request-Id in the response header
"""


if __name__ == "__main__":
    import sys
    import requests

    req = sys.argv[1]
    r = requests.get(req)
    print(r.headers.get("X-Request-Id"))
