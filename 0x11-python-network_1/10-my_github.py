#!/usr/bin/python3
"""
Queries github API
"""
import requests
import sys
if __name__ == "__main__":
    user = requests.get('https://api.github.com/user',
                        auth=(argv[1], argv[2])).json()
    if "id" in user:
        print(user['id'])
    else:
        print(None)
