"""
Write a function that takes one argument,
a positive integer, and returns the sum of its digits.


I: integer
O: integer


Rules:
- return the sum of the digits in the number

DS:
list

Algo:
- make the integer as a string
- iterate over the chars
    - return a list of char as integer again
- return the sum

"""
def sum_digits(num):
    str_num = str(num)

    return sum([int(ch_no) for ch_no in str_num])



# test case
print(sum_digits(23) == 5)              # True
print(sum_digits(496) == 19)            # True
print(sum_digits(123456789) == 45)      # True