#!/usr/bin/python3
"""Returns the list of availabla attributes and methods"""


def lookup(obj):
    """Search for all the attributes and methods of object"""
    return [method for method in dir(obj)]
