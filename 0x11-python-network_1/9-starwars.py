#!/usr/bin/python3
"""
    Sends a search request to Starwars API
"""
import requests
import sys

if __name__ == '__main__':
    val = sys.argv[1] if len(sys.argv) > 1 else ''
    url = 'https://swapi.co/api/people/'
    payload = {'search': val}
    try:
        response = requests.get(url, params=values).json()
        count = response['count']
        print('Number of results: {}'.format(count))
        if count > 0:
            for result in response['results']:
                print (result['name'])
    except ValueError:
        print("Must be JSON")
