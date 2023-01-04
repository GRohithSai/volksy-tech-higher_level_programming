#!/usr/bin/python3
def remove_char_at(str, n):
    if n > len(str):
        return str
    elif n < 0:
        return str
    else:
        s = ""
        temp = list(str)
        temp[n] = s
        str = "".join(temp)
        return str
