#!/usr/bin/python3
"""Class MyList that inherits from list."""


class MyList(list):
    """MyList inherits from list"""

    def print_sorted(self):
        """"Prints list in ascending order"""
        print(sorted(self))

