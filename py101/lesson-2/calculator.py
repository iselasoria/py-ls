<<<<<<< HEAD

"""
Ask the user for the first number.
Ask the user for the second number.
Ask the user for an operation to perform.
Perform the operation on the two numbers.
Print the result to the terminal
"""

=======
>>>>>>> FT-refactor_calc
import time

def prompt(message):
    print(f'==> {message}')

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

print('Welcome to Calculator!')

time.sleep(2)
print()


## main loop mechanism starts here
while True:
    # Ask the user for the first number
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt("Hmm... that doesn't look like a valid number.")
        number1 = input()


    prompt("What is the second number?")
    number2 = input()

<<<<<<< HEAD
prompt("""What operation do you wan to perform?
       1)Add 2)Subtract 3)Multiply 4)Divide""")
operation = input()
=======
    while invalid_number(number2):
        prompt("Hmm... that doesn't look like a valid number.")
        number2 = input()
>>>>>>> FT-refactor_calc

    prompt('What operation do you wan to perform? \n1)Add 2)Subtract 3)Multiply 4)Divide')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

<<<<<<< HEAD
print(f'The result is {output}')
=======
    match operation:
        case '1':
            output = int(number1) + int(number2)
        case '2':
            output = int(number1) - int(number2)
        case '3':
            output = int(number1) * int(number2)
        case '4':
            output = int(number1) // int(number2)

    print(f'The result is {output}')

    prompt('Do you want to run another calculation? (y/n)')
    user_decision = input()
    if user_decision != 'y':
        break
>>>>>>> FT-refactor_calc
