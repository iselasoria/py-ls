"""
Build a program that displays when the user will retire and how many years
she has to work till retirement.

# example
What is your age? 30
At what age would you like to retire? 70

It's 2024. You will retire in 2064.
You have only 40 years of work to go!
"""

from datetime import datetime

print('What is your age?')
age = int(input())

print('At what age do you want to retire?')
retirement = int(input())

current = datetime.now().year
years_left = retirement - age

retirement_year = current + years_left

print(f'You have to work for another {years_left} and will be retired by {retirement_year}.')