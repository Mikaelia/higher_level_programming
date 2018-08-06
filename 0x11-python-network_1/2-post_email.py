#!/usr/bin/python3
"""
Sends a request to a URL, displays the value of the X-Request-Id variable
"""
import urllib.request
import sys

if __name__ == '__main__':
    url, email = (sys.argv[1], sys.argv[2])
    req = urllib.request.Request(url, email.encode('ascii'))
    print(email.encode('ascii'))
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(data.decode('utf-8'))
