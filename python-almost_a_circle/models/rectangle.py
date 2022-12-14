#!/usr/bin/python3
class Rectangle(Base):
    """A class for representing rectangles.

    Private instance attributes:
        __width: The width of the rectangle.
        __height: The height of the rectangle.
        __x: The x-coordinate of the rectangle's top-left corner.
        __y: The y-coordinate of the rectangle's top-left corner.

    Public instance methods:
        width(): Returns the width of the rectangle.
        width(value): Sets the width of the rectangle to value.
        height(): Returns the height of the rectangle.
        height(value): Sets the height of the rectangle to value.
        x(): Returns the x-coordinate of the rectangle's top-left corner.
        x(value): Sets the x-coordinate of the rectangle's top-left corner to value.
        y(): Returns the y-coordinate of the rectangle's top-left corner.
        y(value): Sets the y-coordinate of the rectangle's top-left corner to value.

    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def width(self, value=None):
        if value is None:
            return self.__width
        else:
            self.__width = value

    def height(self, value=None):
        if value is None:
            return self.__height
        else:
            self.__height = value

    def x(self, value=None):
        if value is None:
            return self.__x
        else:
            self.__x = value

    def y(self, value=None):
        if value is None:
            return self.__y
        else:
            self.__y = value
