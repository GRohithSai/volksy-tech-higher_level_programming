#!/usr/bin/python
def multiply_by_2(a_dictionary):
    new = {}
    for i in a_dictionary:
        new[i] = (a_dictionary[i] * 2)
    return (new)
