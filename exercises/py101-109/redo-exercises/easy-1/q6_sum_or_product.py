"""
Write a program that asks the user to enter an integer greater than 0,
then asks whether the user wants to determine the sum or the product
of all numbers between 1 and the entered integer, inclusive.


Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.
---------------------------------------------------------------
Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.

"""

num = int(input('Enter a number greater than 0: '))
computation = input('Enter "s" to computer the sum, or "p" to compute the product: ')
nums_in_range = range(1, num + 1)

def compute_prod(nums):
    res = 1
    for num in nums_in_range:
        res *= num
    return res


if computation == 's':
    print(f"The sum of the integers between 1 and {num} is {sum(nums_in_range)}")
elif computation == 'p':


    print(f"The product of the integers between 1 and {num + 1} is {compute_prod(nums_in_range)}")
