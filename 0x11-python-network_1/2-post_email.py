#!/usr/bin/python3
"""
Sends and email via post
"""
import urllib.request
import urllib.parse
from sys
if __name__ == "__main__":
    info = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(info)
    data = data.encode('ascii')
    url = sys.argv[1]
    reply = urllib.request.Request(url, data)
    with urllib.request.urlopen(reply) as rep:
        body = rep.read()
    print(body.decode(encoding="utf-8"))
