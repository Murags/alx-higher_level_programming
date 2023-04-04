#!/usr/bin/python3

"""
Module that opens a URL and displays the decoded
body of the response. Handles HTTP errors and
displays the error code.
"""

from requests import get
from sys import argv


def main():
    """Opens URL and reads data"""
    url = argv[1]

    try:
        response = get(url)
        response.raise_for_status()
        body = response.text
        print(body)
    except Exception as e:
        print("Error code: {}".format(e))


if __name__ == '__main__':
    """Prevent execution on import"""
    main()
