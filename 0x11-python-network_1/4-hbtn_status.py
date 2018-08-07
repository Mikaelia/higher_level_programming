#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests

    with requests.get('https://intranet.hbtn.io/status') as r:
        print('Body response:\n\t- type: {}\n\t- content: {}'.
              format(type(r.text), r.text))
