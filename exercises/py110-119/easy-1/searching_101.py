"""
Write a program that solicits six (6) numbers from the user and
prints a message that describes whether the sixth number appears
among the first five.
"""
nums = []

print('Enter the 1st number: ')
first = int(input())
nums.append(first)

print('Enter the 2nd number: ')
second = int(input())
nums.append(second)

print('Enter the 3rd number: ')
third = int(input())
nums.append(third)

print('Enter the 4th number: ')
fourth = int(input())
nums.append(fourth)

print('Enter the 5th number: ')
fifth = int(input())
nums.append(fifth)

print('Enter the 6th number: ')
sixth = int(input())

if sixth in nums:
    print(f'{sixth} is in {nums}.')
else:
    print(f'{sixth} isn\'t in {nums}.')