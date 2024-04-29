"""
Write a program that asks for user's name, then greets the user.
If the user appends a ! to their name, the computer will yell the greeting
(print it using all uppercase).


EX1:
What is your name? Sue
Hello Sue.

EX2:
What is your name? Bob!
HELLO BOB! WHY ARE WE YELLING?
"""


print("What is your name? ")
name = input()

if '!' in name:
    print(f'HELLO {name.upper()}! WHY ARE WE YELLING!?')
else:
    print(f'Hello {name}')