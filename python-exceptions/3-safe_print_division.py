#!/usr/bin/python3
def safe_print_division(a, b):
    a = 12
    b = 2
    result = safe_print_division(a, b)
    try:
        print("{:d} / {:d} = {}". format(a, b, result))
    except:
        pass
    finally:
        print("{:d} / {:d} = {}". format(a, b, result))
