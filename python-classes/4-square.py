#!/usr/bin/python3
""" Square - Holbertoon's Python class """


class Square:
    """Init method to instantiation"""
    def __init__(self, size=0):
        self.__size = size


    @property
    def size(self):
        """Getter for size"""
        return self.__size


    @size.setter
    def size(self, value):
        """Setter for size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
