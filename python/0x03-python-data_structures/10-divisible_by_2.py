#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    return [True if i % 2 == 0 else False for i in my_list]

#1st explanation of code
''' In this code, my_list is the list of numbers that you want to check if they are divisible by 2. The function returns a list of booleans where each boolean corresponds to the divisibility of the corresponding element in the input list. '''

#2nd explanation of code
''' The function divisible_by_2 is defined with one parameter, my_list, which has a default value of an empty list [].

The code uses a list comprehension to iterate over each element i in my_list.

For each element i, the code evaluates the condition i % 2 == 0. The % operator calculates the remainder when i is divided by 2. If the remainder is 0, it means that i is divisible by 2.

If the condition i % 2 == 0 is true, the list comprehension assigns the value True to the current element. Otherwise, it assigns the value False.

After iterating over all the elements of my_list, the list comprehension generates a new list of boolean values indicating whether each element in the input list is divisible by 2.

Finally, the new list is returned by the function.

In summary, this code takes a list as input and returns a new list where each element represents whether the corresponding element in the input list is divisible by 2. The resulting list contains boolean values (True or False) corresponding to the divisibility of each element. '''
