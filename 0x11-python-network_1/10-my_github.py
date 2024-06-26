#!/usr/bin/python3
"""
    a Python script that takes your GitHub
    credentials (username and password)
    and uses the GitHub API to display your id

"""


if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
