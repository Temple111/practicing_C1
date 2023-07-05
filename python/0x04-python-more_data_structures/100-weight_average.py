#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    weighted_average = total_score / total_weight
    return weighted_average

#1st explanation 
''' This is a Python function that calculates the weighted average of a list of tuples. The function takes in a list of tuples where each tuple contains two values: the score and the weight. The function then calculates the weighted average by multiplying each score by its corresponding weight, summing up the products, and dividing the sum by the total weight. If the list is empty, it returns 0.

Here is how it works:

The function first checks if the list is empty. If it is, it returns 0.
It then initializes two variables: total_score and total_weight to 0.
It then loops through each tuple in the list and multiplies the score by its corresponding weight and adds it to total_score. It also adds the weight to total_weight.
Finally, it divides total_score by total_weight to get the weighted average. '''

#2nd explanation
''' The weight_average function takes a list my_list as a parameter.

The function begins by checking if my_list is empty using the if not my_list condition. If the list is empty, it means there are no scores and weights to calculate the average, so the function returns 0.

If the list is not empty, the function initializes two variables, total_score and total_weight, to keep track of the cumulative sum of the products of each score and weight.

The function then enters a for loop that iterates over each tuple in my_list. The loop assigns the variables score and weight to each element of the tuple.

Inside the loop, the code multiplies the score by the weight and adds the result to total_score. This step calculates the weighted sum of scores.

Additionally, the code adds the weight to the total_weight variable. This step accumulates the total weight.

After the loop finishes iterating over all the tuples in my_list, the code calculates the weighted average by dividing total_score by total_weight. The result is stored in the weighted_average variable.

Finally, the function returns the calculated weighted_average.

In summary, this code calculates the weighted average of a list of tuples, where each tuple contains a score and its corresponding weight. The function first checks if the list is empty and returns 0 if it is. Then, it iterates over each tuple, calculates the weighted sum of scores and accumulates the total weight. Finally, it calculates and returns the weighted average. '''
