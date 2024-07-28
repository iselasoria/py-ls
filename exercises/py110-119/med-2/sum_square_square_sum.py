"""
Write a function that computes the difference between the
square of the sum of the first count positive integers and
the sum of the squares of the first count positive integers.




I: int
O: int


Rules:
- calculate difference between the square of the sum and the sum of the seuqre of n numbers

Model Solution:
input: 3
(1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)
    36      -       14
return----> 22

DS:
ranges
lists

Algo:

- generate a range from 1 and up to inclusinf the input num and store as n_nums as a list

- take the sum of the list above and square
- take away the sum of a transformed list of squares for each element

"""

def sum_square_difference(num):
    n_nums = list(range(1, num + 1))

    sum_square = sum(n_nums)**2
    square_sum = sum([n**2 for n in n_nums])

    return sum_square - square_sum

# test cases
print(sum_square_difference(3) == 22)          # True
# 22 --> (1 + 2 + 3)**2 - (1**2 + 2**2 + 3**2)

print(sum_square_difference(10) == 2640)       # True
print(sum_square_difference(1) == 0)           # True
print(sum_square_difference(100) == 25164150)  # True