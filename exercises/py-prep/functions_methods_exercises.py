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

