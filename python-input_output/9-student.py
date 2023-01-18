#!/usr/bin/python3
""""9-student Module"""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""
        self.first_name = firstname
        self.last_name = lastname
        self.age = age


    def to_json(self):
        """Get a dictionary representation of the student."""
        return self.__dict__
