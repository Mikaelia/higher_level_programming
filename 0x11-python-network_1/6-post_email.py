#!/usr/bin/python3
"""
Displays the value of the variable X-Request-Id in the response header
"""
if __name__ == '__main__':
    import requests
    import sys

    print(requests.post(sys.argv[1], data={'email': sys.argv[2]}).text)
