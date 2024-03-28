import time
import json

LANGUAGE = 'en'

def prompt(message):
    print(f"==> {message}")

def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False

def messages(message, lang='en'):
    return MESSAGES[lang][message]


with open('messages.json','r') as file:
    MESSAGES = json.load(file)

print(messages('welcome'))

time.sleep(2)
print()


## main loop mechanism starts here
while True:
    # Ask the user for the first number
    prompt("What's the first number?")
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()


    prompt("What is the second number?")
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt('What operation do you wan to perform? \n1)Add 2)Subtract 3)Multiply 4)Divide')
    operation = input()

    while operation not in ["1", "2", "3", "4"]:
        prompt('You must choose 1, 2, 3, or 4')
        operation = input()

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
