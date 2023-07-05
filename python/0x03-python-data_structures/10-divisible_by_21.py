#!/usr/bin/python3 

def divisible_by_2(my_list=[]):
    return[False if i % 2 != 0 else True for i in my_list]  

#the above is the only type of code that can work for this problem ie a boolean way of write this kind of code, it is known as "list comprehension"

#this code did not work def divisible_by_2(my_list=[]):
''' for i in range(len(my_list)):
        if my_list[i] % 2 != 0:
            return[False]
        else:
            return[True]
'''
#Also this did not work
''' def divisible_by_2(my_list=[]):
    for i in my_list:
        if i % 2 != 0:
            return[False]
        else:
            return[True]
'''
