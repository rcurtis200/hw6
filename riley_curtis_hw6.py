#!/usr/bin/env python
"""
Opens an Apache server error log file and finds the top 25 errors
"""
# imports
import sys
from urllib.request import urlopen
# URL for testing: "http://icarus.cs.weber.edu/~hvalle/cs3030/data/error.log.test"


def help():
    print("Usage is: ./riley_curtis_hw6.py <file Input>")


def get_errors(url):
    """
    Opens an Apache server error log file and finds the top 25 errors
    Args:
        url: url for the log
    Returns:
        none
    """
    response = urlopen(url)
    log = response.read().decode('utf-8').split('\n')
    i = 0
    for line in log:
        if i < 25:
            print(line)
        i += 1


def main():
    if len(sys.argv) == 2:
        get_errors(sys.argv[1])
    else:
        help()


if __name__ == '__main__':
    main()
    exit(0)
