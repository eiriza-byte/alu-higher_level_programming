#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Return a list of booleans for whether each integer is even."""
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
