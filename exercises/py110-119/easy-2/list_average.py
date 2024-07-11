"""
Write a function that takes one argument, a list of integers,
and returns the average of all the integers in the list,
rounded down to the integer component of the average.
The list will never be empty, and the numbers will always be
positive integers.


I: list
O: integer

Rules:
- one arg
- return average of all integers in the list, rounded down to the integer component
- list will never me empty
- numbers will be positive integers

Model Solution:
[1, 5, 87, 45, 8, 8]
sum -> 154
len -> 6
avg -> 25.666666
return 25

DS:
list


Algo:
- take the sum of the list and divide by length, use integer division


"""

def average(lst):
    avg = sum(lst) // len(lst)
    return avg

# tests
print(average([1, 5, 87, 45, 8, 8]) == 25)        # True
print(average([9, 47, 23, 95, 16, 52]) == 40)     # True
print(average([7]) == 7)                          # True