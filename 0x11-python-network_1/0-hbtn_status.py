#!/usr/bin/python3
""" fetche https://alx-intranet.hbtn.io/stat """


if __name__ == "__main__":
    import urllib.request

    req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
    with urllib.request.urlopen("https://alx-intranet.hbtn.io/status") as response:
        html = response.read()
    print("Body response:")
    print("\t - type: {}".format(type(html)))
    print("\t - content: {}".format(html))
    print("\t - utf8 content: {}".format(html.decode("utf-8")))
