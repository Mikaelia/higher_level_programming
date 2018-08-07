#!/usr/bin/python3
"""
Displays the value of the variable X-Request-Id in the response header
"""
if __name__ == '__main__':
    import requests
    import sys

    print('Error code: {}'.format(requests.get(sys.argv[1]).status_code))
