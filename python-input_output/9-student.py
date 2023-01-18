#!/usr/bin/python3
""""9-student Module"""


class Student:
    """Representa student."""

    def __init__(self, first_name, last_name, age):
        """Iniatialize a new Student."""

    def to_json(self):
        """Get a dictionary representation of the student."""
        return self.__dict__
