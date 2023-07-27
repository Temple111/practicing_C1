#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        return (self.__size ** 2)

#1st explanation 
'''This is a Python code that defines a class named Square. The class has two methods: __init__ and area.

The __init__ method is a constructor method that initializes the size of the square. It takes one argument, which is the size of the square. If the size is not an integer or if it is less than zero, it raises an error. Otherwise, it sets the size of the square.

The area method calculates the area of the square by squaring its size.

The first line of the code #!/usr/bin/python3 is called a shebang line. It tells the system that this file should be executed using Python 3.'''
