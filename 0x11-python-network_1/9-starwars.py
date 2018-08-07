#!/usr/bin/python3
"""
Sends a search request to Starwars API
"""
import requests
import sys

if __name__ == '__main__':
    val = sys.argv[1] if len(sys.argv) > 1 else ''
    values = {'search': val}
    response = requests.get(
        'https://swapi.co/api/people/',
        params=values).json()
    print('Number of results: {}'.format(response['count']))
    for result in response['results']:
        print (result['name'])
