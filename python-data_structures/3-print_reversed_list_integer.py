#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for i in range(len(digits) // 2):
        digits[i], digits[-1 - i] = digits[-1 -i], digits[i]
        print("{:d"}".format(i))
