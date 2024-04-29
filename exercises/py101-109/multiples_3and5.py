"""
Write a function that computes the sum of all numbers between 1 and
some other number, inclusive, that are multiples of 3 or 5.
For instance, if the supplied number is 20, the result should be
98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

You may assume that the number passed in is an integer greater than 1.
I:
integer

Algo:
generate a list of all numbers in the range
select only those that meet the condition of beign eoither multiples of 3 por 5
sum up all the numbers in the selection above

"""

def multisum(num):
    lst = list(range(1, num + 1))

    valid_mulitples = []

    for i in lst:
        if i % 3 == 0 or i % 5 == 0:
            valid_mulitples.append(i)

    return sum(valid_mulitples)

# test cases
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(1000) == 234168)