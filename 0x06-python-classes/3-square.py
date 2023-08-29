#!/usr/bin/python3
""" Define class square """


class Square:
    """ Description of square """
    def __init__(self, size=0):
        """ initialize size"""

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ Definition of area method"""

        srq = self.__size ** 2
        return srq
