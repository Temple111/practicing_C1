#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    copy = []
    if idx < 0:
        return my_list
    elif idx > len(my_list):
        return my_list
    else:
        for i in my_list:
            copy.append(i)
        copy[idx] = element
        return(copy)
