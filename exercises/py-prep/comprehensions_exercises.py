# 1
# The following code causes an infinite loop (a loop that never stops iterating). Why?
counter = 0

while counter < 5:
    print(counter)

# the reason this is an infinite loop is we never update `counter` and therefore, the condition is always true; 0 will always be less than 5.
    
# 2
    
# Modify the age.py program you wrote in Exercise 6 of the Variables chapter.
# The updated code should use a for loop to display the future ages.
    
"""
age = 22
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')
"""


age = int(input('What is yur age? '))
print(f'Today, you are {age} years old.')

for edad in range(10, 51, 10):
    print(f'In {edad} years, you will be {age + edad} years old.')

# 3
# Use a while loop to print the numbers in my_list, one number per line. Then, do the same with a for loop.
    
my_list = [6, 3, 0, 11, 20, 4, 17]

for num in my_list:
    print(num)

idx = 0
while idx < len(my_list):
    print(my_list[idx])
    idx += 1



# 4
# Use a while loop to print all numbers in my_list with even values, one number per line. 
# Then, print the odd numbers using a ' for' loop.
    
my_list = [6, 3, 0, 11, 20, 4, 17]

idx = 0
while idx < len(my_list):
    if my_list[idx] % 2 == 0:
        print(my_list[idx])
    idx += 1
print()
for num in my_list:
    if num % 2 != 0:
        print(num)

# 5 
# Print all of the even numbers in the following list of nested lists. Don't use any while loops.

my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for lista in my_list:
    for num in lista:
        if num % 2 == 0:
            print(num)

# 6
"""
We'll return to the simpler one-dimensional version of my_list. In this problem, you should write code that 
creates a new list with one element for each number in my_list. If the original number is an even, 
then the corresponding element in the new list should contain the string 'even'; otherwise,
 the element should contain 'odd'.
"""

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

"""# pretty-printed for clarity
[
    'odd', 'odd', 'even', 'odd',
    'even', 'even', 'even', 'odd',
    'odd', 'even', 'even'
]"""
new_list = []

for num in my_list:
    if num % 2 == 0:
        new_list.append('even')
    else:
        new_list.append('odd')
print(new_list)


def odd_or_even(num):
    return 'even' if num % 2 == 0 else 'odd'

res = [odd_or_even(num) for num in my_list]
print(res)


# 7 
# Write a find_integers function that returns a list of all the integers from my_tuple:

my_tuple = (1, 'a', '1', 3, [7], 3.1415,-4, None, {1, 2, 3}, False)

def find_integers(tuple_col):
    return [i for i in tuple_col if type(i) is int]
    # return lista
res = find_integers(my_tuple)

print(res)

# 8 
"""
Write a comprehension that creates a dict whose keys are strings and whose values are the length of the 
corresponding key. Only keys with odd lengths should be in the dict. Use the set given by my_set as the 
source of strings.
"""

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

comprende = {kitty : len(kitty) for kitty in my_set if len(kitty) % 2 != 0}

print(comprende)

# 9 
"""
Write a function that computes and returns the factorial of a number by using a for or while loop. 
The factorial of a positive integer n, signified by n!, is defined as the product of all integers 
between 1 and n, inclusive:"""
def factorial(n):
    result = 1
    for number in range(n, 0, -1):
        result *= number

    return result

# TODO 

print(factorial(1))   # 1
print(factorial(2))   # 2
print(factorial(3))   # 6
print(factorial(4))   # 24
print(factorial(5))   # 120
print(factorial(6))   # 720
print(factorial(7))   # 5040
print(factorial(8))   # 40320
print(factorial(25))  # 15511210043330985984000000

# 10 
"""
The following code uses the randrange function from Python's math library to obtain and print a random integer 
within a given range. Using a while loop, it keeps running until it finds a random number that matches the last 
number in the range. Refactor the code so it doesn't require two different invocations of randrange.
"""

import random

highest = 10
number = random.randrange(highest + 1)
print(number)

while number != highest:
    number = random.randrange(highest + 1)
    print(number)


import random

highest = 10
while True:
    number = random.randrange(highest + 1)
    print(number)
    if number == highest:
        break

# here we are using the do/while construction. It allowes us to execute once, with the opening while True statement, 
#  and then break our of the iteration by using the break statement
    

# 11
# print all the evens without using for loops:

my_list = [
  [1, 3, 6, 11],
  [4, 2, 4],
  [9, 17, 16, 0],
]

idx1 = 0

while idx1 < len(my_list): # look in the main collection
    idx2 = 0
    print(f'Currently processing: {my_list[idx1]}')

    while idx2 < len(my_list[idx1]): # look in the lists inside collection
        if my_list[idx1][idx2] % 2 == 0: # if the number is even
            print(my_list[idx1][idx2]) # print it
        idx2 += 1

    idx1 += 1

