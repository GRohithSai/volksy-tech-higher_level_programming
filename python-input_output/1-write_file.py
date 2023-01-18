#!/usr/bin/python3
# 1-number_of_lines.py
"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """"Return the number of lines in a text file."""
    lines = 0
    with open(filename, encoding='utf-8') as f:
        for line in f:
            lines += 1
    return lines
