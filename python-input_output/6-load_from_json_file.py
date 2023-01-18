#!/usr/bin/python3
"""JSON"""
import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, mode='ri', encoding="UTf-8") as f:
        return (json.load(f))
