#!/usr/bin/python3
"""
Queries github API
"""
import requests
import sys

if __name__ == '__main__':
    url = 'https://api.github.com/user/'
    payload = {'login': sys.argv[1]}
    response = requests.get(url, params=payload,
                            auth=(sys.argv[1], sys.argv[2])).json()
    try:
        print(response['id'])
    except KeyError:
        print('None')
