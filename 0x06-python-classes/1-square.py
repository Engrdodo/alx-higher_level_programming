#!/usr/bin/python3
"""Working with OOP in python"""


class Square():
    """Class representing a square"""

    def __init__(self, size):
        """initiate the class
        
        Args:
            size (int): size of the square
        """
        self.__size = size
        