#!/usr/bin/python3
def inherits_from(obj, a_class):
    '''function'''
    return isinstance(obj, a_class) and not type(obj) == a_class
