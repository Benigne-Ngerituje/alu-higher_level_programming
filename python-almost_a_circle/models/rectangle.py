#!/usr/bin/python3
class Rectangle(Base):
    """A class for representing rectangles."""

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
