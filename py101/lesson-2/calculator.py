import time 
"""
Ask the user for the first number.
Ask the user for the second number.
Ask the user for an operation to perform.
Perform the operation on the two numbers.
Print the result to the terminal
"""
print('Welcome to Calculator!')

time.sleep(2)
print()
# Ask the user for the first number
print("What's the first number?")
number1 = input()

print("What is the second number?")
number2 = input()

print('What operation do you wan to perform? \n1)Add 2)Subtract 3)Multiply 4)Divide')
operation = input()

if operation == '1':
    output = int(number1) + int(number2)
elif operation == '2':
    output = int(number1) - int(number2)
elif operation == '3':
    output = int(number1) * int(number2)
elif operation == '4':
    output = int(number1) // int(number2)

print(f'The result is {output}')