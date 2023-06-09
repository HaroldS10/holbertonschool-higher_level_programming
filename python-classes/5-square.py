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
        if (isinstance(value, int) is False):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    """ My_print - Prints the square using # """
    def my_print(self):
        if (self.size == 0):
            print()
        for height in range(self.size):
            for length in range(self.size):
                print("#", end="")
            print()
