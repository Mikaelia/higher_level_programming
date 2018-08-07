#!/usr/bin/python3
"""
Queries github API
"""
import requests
import sys

if __name__ == '__main__':
    payload = (sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user/',
                            auth=payload).json()
    if 'id' in response:
        print(response['id'])
    else:
        print('None')
