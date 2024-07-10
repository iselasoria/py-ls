"""
Write a function that takes a list of positive integers as input, multiplies all of the integers together,
divides the result by the number of entries in the list, and returns the result as a string with the
value rounded to three decimal places.



I: list of integers
O: string

Rules:
- take avg but multiplying instead of adding
- rount to three places
- convert to string

DS:
str

Algo:
- initialize product to 1
- iterate over list
    - with each iteration
        - multiply the product *= the element at that position
- divide producct by thr length of the original list
** important to not use integer division
- string format to three decimals

"""

def multiplicative_average(lst):
    product = 1

    for i in lst:
        product *= i

    avg = product / len(lst)
    return "{:.3f}".format(avg)


# All of these examples should print True
print(multiplicative_average([3, 5]) == "7.500")
print(multiplicative_average([2, 5, 8]) == "26.667")
print(multiplicative_average([2, 5]) == "5.000")
print(multiplicative_average([1, 1, 1, 1]) == "0.250")
print(multiplicative_average([2, 5, 7, 11, 13, 17]) == "28361.667")