#!/usr/bin/python3
"""
Sends letter as a post and displays JSON
"""
if __name__ == '__main__':
    import requests
    import sys

    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ''
    try:
        response = requests.post(
            'http://0.0.0.0:5000/search_user',
            data={
                'q': letter}).json()
        if 'id' in response and 'name' in response:
            print('[{}] {}'.format(response['id'], response['name']))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
