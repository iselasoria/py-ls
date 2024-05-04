"""
Write a program that prompts the user for two positive numbers
(floating-point), then prints the results of the following
operations on those two numbers: addition, subtraction,
product, quotient, floor quotient, remainder, and power.
Do not worry about validating the input.

==> Enter the first number:
3.141529
==> Enter the second number:
2.718282
==> 3.141529 + 2.718282 = 5.859811
==> 3.141529 - 2.718282 = 0.42324699999999993
==> 3.141529 * 2.718282 = 8.539561733178
==> 3.141529 / 2.718282 = 1.1557038600115808
==> 3.141529 // 2.718282 = 1.0
==> 3.141529 % 2.718282 = 0.42324699999999993
==> 3.141529 ** 2.718282 = 22.45792517468373
"""

print("Enter a number in decimal format:")
num1 = float(input())

print("Enter the second decimal number: ")
num2 = float(input())

print(f'{num1} + {num2} = {num1 + num2}')
print(f'{num1} - {num2} = {num1 - num2}')
print(f'{num1} * {num2} = {num1 * num2}')
print(f'{num1} / {num2} = {num1 / num2}')
print(f'{num1} // {num2} = {num1 // num2}')
print(f'{num1} % {num2} = {num1 % num2}')
print(f'{num1} ** {num2} = {num1 ** num2}')

