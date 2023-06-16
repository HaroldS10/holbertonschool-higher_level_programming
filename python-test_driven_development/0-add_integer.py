#!/usr/bin/python3
"""adds 2 integers"""


def add_integer(a, b=98):
    """Adds two integers.
        Arguments:
        Datatypes
    """
    if type(a) is not [int, float]:
        raise TypeError("a must be an integer")
    if type(b) is not [int, float]:
        raise TypeError("b must be an integer")
    
    """Return: sum of the two integers"""
    return (int(a) + int(b))
