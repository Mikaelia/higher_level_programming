#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import urllib.request

    req = urllib.request.Request('https://intranet.hbtn.io/status')
    with urllib.request.urlopen(req) as response:
        data = response.read().decode('utf-8')
        print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(data), data))
