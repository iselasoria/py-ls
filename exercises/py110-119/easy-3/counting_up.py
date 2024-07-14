"""
Write a function that takes an integer argument and returns a
list containing all integers between 1 and the argument
(inclusive), in ascending order.

You may assume that the argument will always be a positive
integer.

I: int
O: list

Rules:
- result contains all integers between 1 and the arg
- argument is inclusive
- ascending order

DS:
list

Algo:
- generate a range from 1 to argument + 1
- turn range object into list and return


"""

def sequence(num):
    r = range(1, num + 1)
    return list(r)

# test cases
print(sequence(5)== [1, 2, 3, 4, 5])   # True
print(sequence(3) == [1, 2, 3])         # True
print(sequence(1) == [1])               # True