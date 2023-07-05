#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n >= len(str):
        return str

    result = ""
    for i in range(len(str)):
        if i != n:
            result += str[i]

    return result
#Explanation:
# The function remove_char_at takes two parameters: string, which is the input string, and n, which is the position of the character to be removed.
# We start by checking if the value of n is within the valid range for the given string. If n is less than 0 or greater than or equal to the length of the string, we return the original string since there is no character to remove.
# We initialize an empty string result to store the modified string without the character at position n.
# We iterate over the indices of the input string using a for loop and the range() function.
# Inside the loop, we check if the current index i is equal to n. If they are equal, we skip adding that character to the result string.
# If i is not equal to n, we concatenate the character at position i in the original string to the result string.
# Finally, we return the result string, which is a copy of the original string with the character at position n removed.
