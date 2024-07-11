"""
You want to multiply all elements of a list by 2. However,
the function is not returning the expected result. Explain the bug,
and provide a solution.
"""

def multiply_list(lst):
    for item in lst:
        item *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# SOLUTION
# the issue with the code above is that we are not using indexed reassignment to modufy the list object a
# and we are also not using a list comprehension to transform a new list. All this code is doing is
# iterating over the list and in each iteration multioplying the variable item used in the iteration and multiplying by 2
# but that does absolutely nothing. We can use a list comprehansion to return a new list.

def multiply_list(lst):
    return [item * 2 for item in lst]

print(multiply_list([1, 2, 3]) == [2, 4, 6])

# or we can use idnexed re-assignmetn to modify the list in place
def multiply_list(lst):
    for idx, item in enumerate(lst):
        lst[idx] *= 2

    return lst

print(multiply_list([1, 2, 3]) == [2, 4, 6])