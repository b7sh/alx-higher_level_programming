#!/usr/bin/python3
"""
    takes in a URL and an email address,
    sends a POST request to the passed URL
    with the email as a parameter,
    and finally displays the body of the response.
"""


if __name__ == "__main__":
    import sys
    import requests

    req = sys.argv[1]
    params = {"email": sys.argv[2]}
    r = requests.post(req, data=params)
    print("{}".format(r.text))
