"""
Write a program that asks the user to enter an integer greater than 0,
then asks whether the user wants to determine the sum
or the product of all numbers between 1 and the entered integer, inclusive.

EX2:
Please enter an integer greater than 0: 5
Enter "s" to compute the sum, or "p" to compute the product. s

The sum of the integers between 1 and 5 is 15.

EX2:
Please enter an integer greater than 0: 6
Enter "s" to compute the sum, or "p" to compute the product. p

The product of the integers between 1 and 6 is 720.
"""
def consec_sum(num):
    r_list = list(range(1,num + 1))
    print(r_list)
    return sum(r_list)

def consec_prod(num):
    r_list = list(range(1, num + 1 ))

    result = 1

    for i in r_list:
        result *= i

    return result


print('Let\s play a math game. Enter a number as your top of the range: ')
top_range = int(input())


print('Enter 1 for a consecutive sum, or 2 for a consecutive prodiuct: ')
choice = int(input())
if choice == 1:
    operation = consec_sum(top_range)
    print(f'The sum of your range is {operation}.')
elif choice == 2:
    operation = consec_prod(top_range)
    print(f'The product of your range is {operation}')
else:
    print('Please only enter either 1 or 2:')

print()
