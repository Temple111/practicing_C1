#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

#1st explanation
''' This is a Python code that defines a class named Square. The class has an instance variable named __size which is initialized to 0 by default. The class also has a constructor method named __init__ which takes an argument named size. If the argument passed is not an integer, it raises a TypeError exception with the message “size must be an integer”. If the argument passed is less than 0, it raises a ValueError exception with the message “size must be >= 0”. Otherwise, it sets the instance variable __size to the value of the argument passed.

The first line of the code (#!/usr/bin/python3) is called a shebang line. It tells the operating system that this file should be executed using the Python 3 interpreter. '''
