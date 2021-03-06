#!/usr/bin/python3
class Square():
    '''
        Creates a Square
    '''

    def __init__(self, size=0):
        '''Initialization of the square with size'''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Calculates the area'''
        return self.__size * self.__size
        '''Return: The current square area.'''

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''Updating the private attributes'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
