#!/usr/bin/python3
"""
Submits a post requeset with a specific email
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    req = urllib.request.Request(url)
    try:
        urllib.request.urlopen(req)
    except urllib.error.HTTPError as e:
        print('Error code: {}'.format(e.code))
    print(req.decode('utf-8'))
