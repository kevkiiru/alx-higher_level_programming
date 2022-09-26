#!/usr/bin/python3
"""Module base_geometry. Finding public instance methods.
"""


class BaseGeometry:
    """Class BaseGeometry."""

    def area(self):
        """area of the geometry"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """value: the one to validated"""
        if value is not int:
            raise TypeError("<name> must be an integer")
        if value >= 0:
            raise TypeErro("<name> must be greater than 0")
