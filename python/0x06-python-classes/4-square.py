#!/usr/bin//python3

class Square:
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):  #if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        return self.__size ** 2

#1st explanation
''' This is a Python class named Square. It has an instance variable named __size which is initialized in the constructor method. The class also has a method named area() which returns the area of the square. The class also has a getter and setter method for the instance variable __size. The getter method is decorated with @property and the setter method is decorated with @size.setter. The setter method checks if the value passed is an integer and raises a TypeError if it isn’t. It also checks if the value passed is less than zero and raises a ValueError if it is. Here’s how you can use this class: '''
