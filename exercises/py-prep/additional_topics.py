# 1 
# What does the following function do? Be sure to identify the output value.

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()
# first, Python will identify the bare bones structure it can perform any operation on, in this case they dictionary. It calls .keys on it and extracts a list of keys, so now we have:
# ['Karl','Clare','Karis','Trevor','Anotnia','Chris'] and then sorts the list, so now we have
# ['Anotnia', 'Chris','Clare','Karl','Karis','Trevor'] then it will 
# accesses the second element--> 'Chris'. Now, it will upcase the string --> 'CHRIS'
my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))


# 2
# Write some code to output the square root of 37. Try to write the code in three different ways.

import math 

res = math.sqrt(37)
print(res)

###########

from math import sqrt 
res = sqrt(37)
print(res)

############

import math as m 

res = m.sqrt(37)
print(res)

# 3 
# consider the following:
def sum_of_squares(num1, num2):

    def square(number): ## solution
        return number * number

    return square(num1) + square(num2)

print(sum_of_squares(3, 4))   # 25 (3 * 3 + 4 * 4)
print(sum_of_squares(5, 12))  # 169 (5 * 5 + 12 * 12)
# 


# Write a nested function in sum_of_squares that will make this code work as shown.


# 4
# Write a function called increment_counter that increments a counter variable every time it is called. You can test your code with the following:

counter = 0 

def increment_counter():
    global counter 
    counter += 1

print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101

# 5 
# On reflection, we've decided that we don't want to rely on using a global variable in the code we 
# wrote in the previous example. To fix this, we're going to nest the code from the previous example 
# into an outer function:

def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter # global keyword only works on global variables, if inside a nested function we must use nonlocal
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()