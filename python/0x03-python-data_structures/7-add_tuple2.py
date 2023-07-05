#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        tuple_a = tuple_a + (0,)*(2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b = tuple_b + (0,)*(2 - len(tuple_b))

    return(tuple(map(lambda i, j: i + j, tuple_a, tuple_b)))


#How to pad a tuple
''' #original_tuple = (1, 2, 3)
desired_length = 5
padding_element = 0

# Calculate the number of elements needed for padding
padding_count = desired_length - len(original_tuple)

# Create the padding tuple
padding_tuple = (padding_element,) * padding_count

# Concatenate the original tuple with the padding tuple
padded_tuple = original_tuple + padding_tuple

print(padded_tuple)'''
