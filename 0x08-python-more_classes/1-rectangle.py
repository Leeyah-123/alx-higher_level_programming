#!/usr/bin/python3
""" A module that defines a rectangle """


class Rectangle:
    """ This is a class that defines a rectangle """
    __width
    __height

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def width(self):
        return (self.width)

    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.width = value

    def height(self):
        return (self.height)

    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.height = value
