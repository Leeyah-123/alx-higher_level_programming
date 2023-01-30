#!/usr/bin/python3
""" A module that defines a rectangle """


class Rectangle:
    """ This is a class that defines a rectangle """

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """ method that returns the value of the width

        Returns:
            width of the rectangle

        """

        return self.__width

    @width.setter
    def width(self, value):
        """ method that sets the value of the width

        Args:
            value: Value to set width to

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """ method that returns the height of the rectangle

        Returns:
            height of the rectangle

        """

        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
