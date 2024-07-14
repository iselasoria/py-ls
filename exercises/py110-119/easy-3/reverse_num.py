"""
Write a function that takes a positive integer as an argument
and returns that number with its digits reversed.

I: positive integer
O: integer

Rules:
- reverse the digits
- 0s don't to count when they are on the left

Model Solution:
- 12345 --> 54321
- 12000 --> 00021 --> 21

DS:
interim: list?

Algo:
- turn number into string
- reverse the string as list
- turn back into integer and return

"""
def reverse_number(num):
    num_str = str(num)
    return int(num_str[::-1])

# test cases
print(reverse_number(12345) == 54321)   # True
print(reverse_number(12213) == 31221)   # True
print(reverse_number(456) == 654)       # True
print(reverse_number(1) == 1)           # True
print(reverse_number(12000) == 21)      # True