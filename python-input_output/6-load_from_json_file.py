#!/usr/bin/python3
"""JSON"""
import json


def load_from_json_file(filename):
    """Create object from a JSON file"""
    with open(filename, mode="r", encoding="UTf-8") as f:
        return (json.loads(f))
