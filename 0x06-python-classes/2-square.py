#!/usr/bin/python3
class Square():
    '''
        Creates a Square
    '''

    def __init__(self, size=0):
        '''Initialization of the square with size'''

            '''size: Zero or positve number.'''
        if not isinstance(size, int):
            raise TypeError("size is an integer")
        if size < 0:
            raise ValueError("size is >= 0")
        self.__size = size
