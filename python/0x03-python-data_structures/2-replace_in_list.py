#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    if (idx < 0):
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        my_list[idx] = element  # u dont need to iterate when trying to replace a list content at an index bcos the program will think u are trying to retrieve the item                                  at that index.
        return my_list
