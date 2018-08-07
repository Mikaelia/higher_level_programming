#!/usr/bin/python3
"""
Displays the value of the variable X-Request-Id in the response header
"""
if __name__ == '__main__':
    import requests
    import sys

    response = requests.get(sys.argv[1])
    error = response.error_code
    if error > 400:
            print('Error code: {}'.format(error))
    else:
        print(response.text)
