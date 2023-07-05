#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])


#1st explanation of code
''' This is a Python code that defines a function called multiple_returns that takes in a string argument called sentence. The function checks if the length of the sentence is zero. If it is zero, the function returns a tuple containing 0 and None. If the length of the sentence is not zero, the function returns a tuple containing two values: the length of the sentence and the first character of the sentence. '''

#2nd explanation of code
''' The function multiple_returns is defined with one parameter, sentence.

The first line of code checks if the length of the sentence is equal to 0. This is done using the len() function. If the length is indeed 0, it means that the sentence is empty.

If the sentence is empty, the code executes the first return statement. The return statement returns a tuple (0, None). This tuple represents the case where the sentence is empty, with the first element being 0 and the second element being None.

If the sentence is not empty, meaning it has at least one character, the code executes the else block.

In the else block, the code executes the second return statement. This return statement also returns a tuple, but with different values. The first element of the tuple is the length of the sentence, calculated using the len() function. The second element is the first character of the sentence, accessed using the index [0].

After executing either the first or second return statement, the function exits and returns the corresponding tuple.

In summary, this code takes a sentence as input and returns a tuple. If the sentence is empty, the tuple (0, None) is returned. If the sentence is not empty, the tuple contains the length of the sentence as the first element and the first character of the sentence as the second element.'''
