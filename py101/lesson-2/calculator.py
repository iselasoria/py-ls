import time 

def prompt(message):
    print(f'==> {message}')


"""
Ask the user for the first number.
Ask the user for the second number.
Ask the user for an operation to perform.
Perform the operation on the two numbers.
Print the result to the terminal
"""
prompt('Welcome to Calculator!')

time.sleep(2)
print()
# Ask the user for the first number
prompt("What's the first number?")
number1 = input()

prompt("What is the second number?")
number2 = input()

prompt('What operation do you wan to perform? \n1)Add 2)Subtract 3)Multiply 4)Divide')
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