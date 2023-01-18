#!/usr/bin/python3
# 2-read_lines.py
"""Defines a text file-reading function."""


def append_write(filename="", text=""):
    """Print a given number of lines from a UTF8 text file to stdout."""
    if filename:
        with open(filename, mode='a', encoding="utf-8") as f:
            return (f.write(text))
