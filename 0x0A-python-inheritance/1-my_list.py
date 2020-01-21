#!/usr/bin/python3
'''function to inherit from list class'''


class MyList(list):

    def print_sorted(self):
        print(sorted(self))
