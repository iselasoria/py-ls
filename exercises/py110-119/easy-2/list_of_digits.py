"""
Write a function that takes one argument, a positive integer,
and returns a list of the digits in the number.

I: int
O: list

DS:
list

Algo:
iterate over the string char and return the integer one by one in a list comprehension


"""

def digit_list(num):
    return [int(digit) for digit in str(num)]

# test cases
print(digit_list(12345)== [1, 2, 3, 4, 5])       # True
print(digit_list(7) == [7])                       # True
print(digit_list(375290) == [3, 7, 5, 2, 9, 0])   # True
print(digit_list(444) == [4, 4, 4])               # True