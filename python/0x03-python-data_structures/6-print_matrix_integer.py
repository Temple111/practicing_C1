#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                print("{:d}".format(row[i]), end="")
            else:
                print("{:d}".format(row[i]), end=" ")
        print()

#1st explanation of code
''' This is a Python code that defines a function called print_matrix_integer that takes an optional argument called matrix. The function prints the matrix in a specific format. It first loops through each row in the matrix and then loops through each element in the row. If the element is the last element in the row, it prints it without any space after it. Otherwise, it prints the element followed by a space. After printing all elements in a row, it prints a newline character to move to the next line. '''

#2nd explanation of code
''' The function print_matrix_integer is defined with one parameter, matrix, which has a default value of an empty matrix [[]].

The code uses nested for loops to iterate over each row in the matrix list.

For each row, an inner for loop is used to iterate over the elements of that row. The loop variable i represents the index of the current element within the row.

Within the inner loop, an if statement checks if the current element is the last element in the row. This is done by comparing i with len(row) - 1, where len(row) gives the total number of elements in the row. If i is equal to len(row) - 1, it means the current element is the last one in the row.

If the current element is the last one in the row, the code prints the element using the print() function and the end parameter set to an empty string (""). This ensures that there is no newline character at the end of the print statement.

If the current element is not the last one in the row, the code prints the element followed by a space using the print() function and the end parameter set to a space character (" "). This separates each element with a space.

After printing all the elements in a row, the code calls print() with no arguments. This prints a newline character, causing the next row to be printed on a new line.

The outer loop then continues to the next row, and the process repeats until all rows in the matrix have been printed.

In summary, this code takes a matrix as input and prints its elements in a formatted manner, with each element separated by a space within a row and each row printed on a new line.'''
