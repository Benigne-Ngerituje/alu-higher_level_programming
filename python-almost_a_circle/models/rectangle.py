#!/usr/bin/python3

"""Rectangle Instance classes"""

from models.base import Base


class Rectangle(Base):

    """A class for representing rectangles."""

    def __init__(self, width, height, x=0, y=0, id=None):

        """ initializing a new width, height, x value, y value and id """
        
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def width(self, value=None):

        """ assigning a value to width """

        if value is None:
            return self.__width
        else:
            self.__width = value

    def height(self, value=None):

        """ assigning a value to height """

        if value is None:
            return self.__height
        else:
            self.__height = value

    def x(self, value=None):

        """ assigning a value to x """

        if value is None:
            return self.__x
        else:
            self.__x = value

    def y(self, value=None):

        """ assigning a value to y """
        if value is None:
            return self.__y
        else:
            self.__y = value
