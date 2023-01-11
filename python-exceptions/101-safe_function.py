#!/usr/bin/python3
def safe_function(fct, *args):
    from sys import stderr
    try:
        return (fct(*args))
    except Exception a err:
        print("Excption: {}".format(err), file=stderr)
        return None
