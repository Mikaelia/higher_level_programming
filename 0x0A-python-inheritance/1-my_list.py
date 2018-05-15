#!/usr/bin/python3
class MyList(list):
    """ Creates class MyList that inherits from list
    """
    def print_sorted(self):
        print(list(sorted(self)))
