#!/usr/bin/python3
"""
Displays the value of the variable X-Request-Id in the response header
"""
if __name__ == '__main__':
    import requests
    import sys

    try:
        response = requests.get(sys.argv[1])
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.HTTPError as e:
        print('Error code: {}'.format(e.response.status_code))
