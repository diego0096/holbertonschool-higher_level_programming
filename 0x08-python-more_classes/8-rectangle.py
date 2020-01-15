#!/usr/bin/python3
class Rectangle:
    '''Create rectangle'''

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        symbol = str(self.print_symbol)
        rectangle = ""
        if self.height == 0 or self.width == 0:
            return rectangle

        for h in range(self.height - 1):
            rectangle += symbol * self.width + "\n"
        rectangle += symbol * self.width
        return rectangle

    def __repr__(self):
        '''creating a recreation of the instance call'''
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        '''printing a message with instance is deleted'''
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Checks if the rectangles are bigger or equal."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
