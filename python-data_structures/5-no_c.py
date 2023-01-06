#!/usr/bin/python3
def no_c(my_string):
    li = []
    for i in my_string:
        if i != 'c' and i != 'C':
            li.append(i)
    return "".join(li)
