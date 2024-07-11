"""
We defined a function intending to multiply the sum of numbers by a factor.
However, the function raises an error. Why? How would you fix this code?
"""

# def sum(numbers, factor):
#     return factor * sum(numbers)

# numbers = [1, 2, 3, 4]
# print(sum(numbers, 2) == 20)

# SOLUTUON
# the issue here is we are re-using the `sum` variable name for our function, but
# python already has a `sum` built-in function and we are essentially overriding it
# so if we run it as is, we get an error indicating our call on the second line is missing
# an additional argument, in this case, `factor`. We can correct by renaming our function:

def multiply_sum(numbers, factor):
    return factor * sum(numbers)

numbers = [1, 2, 3, 4]
print(multiply_sum(numbers, 2) == 20) # True