#!/usr/bin/python3
class Rectangle:
    '''Create rectangle'''

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        '''returns the rectangle area'''
        return self.__width * self.__height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        '''returns the rectangle perimeter'''
        return 2 * (self.__width + self.__height)

    def __str__(self):
        '''returning the string representation of the rectangle'''
        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle

        for h in range(self.height - 1):
            rectangle += "#" * self.width + "\n"
        rectangle += "#" * self.width
        return rectangle

    def __repr__(self):
        '''creating a recreation of the instance call'''
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        '''printing a message with instance is deleted'''
        print("Bye rectangle...")
