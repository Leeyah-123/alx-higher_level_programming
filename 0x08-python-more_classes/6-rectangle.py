#!/usr/bin/python3
""" A module that defines a rectangle """


class Rectangle:
    """ This is a class that defines a rectangle """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle

        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """ method that sets the height

        Raises:
            TypeError: if the height is not an integer
            ValueError: if the height is less than 0

        """

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """ method that returns the area of the rectangle

        Returns:
            area of the rectanglw

        """

        return self.height * self.width

    def perimeter(self):
        """ method that returns the perimeter of the rectangle

        Returns:
            perimeter of the rectangle

        """

        if self.width == 0 or self.height == 0:
            return 0

        return (2 * (self.width + self.height))

    def __str__(self):
        """ method that returns the rectangle #

        Returns:
            The # of a rectangle

        """

        rectangle = ""

        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(self.height):
            rectangle += ("#" * self.width) + "\n"

        return rectangle[:-1]

    def __repr__(self):
        """ method that returns the string representation of the instance

        Returns:
            string representation of the object

        """

        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """ method that prints a message on deletion of an instance """

        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
