# what happens whenyou run the following? Why?
def set_foo():
    foo = 'bar'

set_foo()
print(foo)

# SOLUTION
"""
The code will raise an exception because the variable `foo` is out of scope when 
# it is called on line 6
"""

# 2
# what does this print and why?

foo = 'bar'

def set_foo():
    foo = 'qux'

set_foo()
print(foo)
"""
This program prints out `bar` because the variable `foo` is local to the function definition
so when we use it on line 20, even though it might appear appear like reassignemnt, it is not because 
the function does not have access to the `foo` defined outside the function definition.


"""

# #3
# Write a program that uses a multiply function to multiply two numbers 
# and returns the result. Ask the user to enter the two numbers, 
# then output the numbers and result as a simple equation.



def multiply():
    n1 = input('Enter the first number: ')
    n2 = input('Enter the second number: ')
    print(f'{n1} * {n2} =  {float(n1) * float(n2)}')

multiply() #3.1416, 2.7183)

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

# 4 
# Consider the following code:
def multiply_numbers(num1, num2, num3):
    result = num1 * num2 * num3
    return result

product = multiply_numbers(2, 3, 4)

# identify the following code:

# function name -----------> mutlitply_numbers
# function arguments ------> 2,3,4
# function definition -----> starting with def and ending in the return statement
# function body -----------> results = num1 * num2 * num3
                          #  return result
# function parameters -----> num1, num2, num3
# function invocation -----> multiply_numbers
# function return value ---> result
# all identifiers ---------> multoiply_numbers, result, num1, num2, num3, product

# 5 
# what does this code print?
def scream(words):
    return words + '!!!!'

scream('Yipeee')

# the code does not output anything, there is no call to the print statement


# 6 
# what does the following code print?
def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# this code does not print anything, the explicit return termiantes the program
# before it reaches the print statement

# 7
# without running it, what do you think the following code will do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo('Hello')

# this raises an exception because we defined the function with two paramters
# but we are calling it with jsut one


# 8
# what will this code do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718)

# this will raise an error, we defined the method with two parameters but are attempting to pass
# three arguments. Python doesnt know how to handle that and raises and error


# 9
# what will this code do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592, 2.718)
# 42
# 3.1416
# 2.718
# because we explicitly passed in all the three arguments the function was
# designed to take, we don't actually use any of the defaults


# 10
# what will this code do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42, 3.141592)

# 42
# 3.1416
# 2

# 11
# what will this code do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo(42)

# 42
# 3
# 2

# the function is defiend with three params but we only pass in one arg. 
# this works regardless because we defined default arguments for those params, that is
# why it works


# 12
# what will the code do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo()

# this will raise an error because the function is designed to take three
# arguments and at least one of thoise has not been defined with a default value


# 13 
# what will this doe?
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42)

# this raises an error because we only pass in the first positional arg, then we rely on the default for the second arg
# but there is no default for the third


# 14
# identify all the indetifiers:

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')


# multiply, get_nun, left, right, prompt, first_numbers, second_number and product


# 15
# classify all the identifiers as global, local or built-in 
def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# global
    # multiply 
    # get_num
    # first_number
    # second_number
    # product 
# local
    # left
    # right
    # prompt 

# built-in 
    # float 
    # input 
    # print 

# 16

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# identify function names and params
# functions
    # multiply 
    # get_num 

# params 
    # left
    # right 
    # prompt 

# 17
# which are function names, method names and which are builtin functions?

def say(message):
    print(f'==> {message}')

string1 = input()
string2 = input()

say(max(string1.upper(), string2.lower()))

# functions
    # say
    # though technically, all of them are functions.
    # every method is a funciton but not every function is a method

# methods 
    # .upper()
    # .lower()
# built-in functions
    # max
    # print
    # input


# 18

# The following function returns a list of the remainders of dividing the numbers in numbers by 3:




def remainders_3(numbers):
    return [number % 3 for number in numbers]
"""
    Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):"""

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []



def remainders_3(numbers):
    return [number % 3 for number in numbers]

print(any(remainders_3(numbers_1)))
print(any(remainders_3(numbers_2)))
print(any(remainders_3(numbers_3)))
print(any(remainders_3(numbers_4)))


# 19

