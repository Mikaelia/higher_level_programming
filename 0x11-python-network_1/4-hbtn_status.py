#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status
"""
if __name__ == '__main__':
    import requests

    text = requests.get('https://intranet.hbtn.io/status').text
    print('Body response:\n\t- type: {}\n\t- content: {}'.format(type(text), text))
