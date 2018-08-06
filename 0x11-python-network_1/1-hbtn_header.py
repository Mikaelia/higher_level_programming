#!/usr/bin/python3
"""
Sends a request to a URL, displays the value of the X-Request-Id variable
"""
import urllib.request
import sys

req = urllib.request.Request(sys.argv[1])
with urllib.request.urlopen(req) as response:
    content = response.info()
    print(content['X-Request-Id'])
