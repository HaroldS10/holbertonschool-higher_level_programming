#!/usr/bin/python3
""" Square - Holbertoon's Python class """


class Square:
    """Init method to instantiation"""
    def __init__(self, size=0):
        if (isinstance(size, int) is False):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
