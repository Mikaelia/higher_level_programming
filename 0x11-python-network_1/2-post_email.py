#!/usr/bin/python3
"""
    Sends and email via post
"""

if __name__ == '__main__':
    import urllib.request
    import utllib.parse
    import sys

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('utf-8')
    request = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode(encoding='utf-8'))
