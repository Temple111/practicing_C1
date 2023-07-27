#!/usr/bin/python3
''' Here is an example of a Python class Square that defines a square by:

A private instance attribute: size
Instantiation with size (no type/value verification)
No importation of any module '''

class Square:
    """A class with a private instance attribute with a method that uses this attribute"""
    def __init__ (self, size=0):
        """Instantiate size attribute"""
        self.__size = size  # The line of code “self.__size = size” is initializing a private instance attribute called “__size” with the value of “size”. This attribute can only be accessed within the class

#1st explanation
''' This is a Python class called Square. It has a private instance attribute called __size which is initialized in the constructor method __init__. The double underscore prefixing the attribute name makes it private. Private attributes are not supposed to be accessed from outside the class. They can only be accessed within the class itself. The purpose of making an attribute private is to prevent accidental modification of the attribute by external code. '''

