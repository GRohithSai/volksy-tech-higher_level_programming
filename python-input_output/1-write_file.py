#!/usr/bin/python3
# 1-number_of_lines.py
"""Defines a text file line-counting function."""


def write_file(filename="", text=""):
    """"Return the number of lines in a text file."""
    if filename:
        with open(filename, mode='w', encoding='utf-8') as f:
            return (f.write(text))
