#!/usr/bin/python3
""" Define class square """


class Square:
    """ Description of square """

    def __str__(self):
        """ print my way """

        return self.pos_print()[:-1]

    def __init__(self, size=0, position=(0, 0)):
        """Create a square"""

        self.size = size
        self.position = position

    @property
    def size(self):
        """ get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """ set size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ position """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        if len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if len([i for i in value if isinstance(i, int) and i >= 0]) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """ Definition of area method"""

        srq = self.__size * self.__size
        return srq

    def pos_print(self):
        """returns the position in spaces"""
        pos = ""
        if self.size == 0:
            return "\n"
        for w in range(self.position[1]):
            pos += "\n"
        for w in range(self.size):
            for i in range(self.position[0]):
                pos += " "
            for j in range(self.size):
                pos += "#"
            pos += "\n"
        return pos

    def my_print(self):
        """print the square in position"""
        print(self.pos_print(), en
