#Q1
"""
Here's an exercise for you: suppose we wanted to transform the numbers
based on their position in the list rather than their value?
Try coding a solution that doubles the numbers that have odd indexes:

I: list
O: list

Rules:
- double the numbers at odd indexes only
- leave numbers at even indexes as is

Model Solution:
       [2,5,1,7]
idx:    0 1 2 3
return:[2, 10, 1, 14]

"""

def double_odd_idx(lst):
    doubled_idx = []

    for idx, num in enumerate(lst):
        # print(f'The number {num} is at index: {idx}')
        if idx % 2 != 0:
            doubled_idx.append(num * 2)
        else:
            doubled_idx.append(num)

    return doubled_idx

print(double_odd_idx([2,5,1,7])) # [2, 10, 1, 14]

## Q2
"""
Modify the function above to make a new funciton `multiply` that allows
you to transform by multiplying by an arbitrary number given by an argument
and returning a new list.
"""

def multiply(lst, factor):
    multiplied_idx = []

    for idx, num in enumerate(lst):

        if idx % 2 != 0:
            multiplied_idx.append(num * factor)
        else:
            multiplied_idx.append(num)

    return multiplied_idx

print(multiply([2,5,1,7], 3)) # [2, 15, 1, 21]

