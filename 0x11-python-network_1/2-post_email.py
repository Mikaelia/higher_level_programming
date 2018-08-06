!/usr/bin/python3
"""
Submits a post requeset with a specific email
"""
import urllib.request
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    values =  {'email': sys.argv[2]}
    url_values = urllib.parse.urlencode(values)
    req = urllib.request.Request(url, url_values.encode('utf-8'))
    with urllib.request.urlopen(req) as response:
        data = response.read()
        print(data.decode('utf-8'))
