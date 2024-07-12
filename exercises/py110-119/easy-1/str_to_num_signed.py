import re

"""
In the previous exercise, you developed a function that converts simple
numeric strings to integers. In this exercise, you're going to extend
that function to work with signed numbers.

Write a function that takes a string of digits and returns the appropriate
number as an integer. The string may have a leading + or - sign; if the
first character is a +, your function should return a positive number;
if it is a -, your function should return a negative number.
If there is no sign, return a positive number.

You may assume the string will always contain a valid number.
You may not use any of the standard conversion functions available in Python,
such as int. You may, however, use the string_to_integer function from
the previous exercise.

Algo:
- take the string and strip any characters that are not digits, this will be used for the function as it was in the previous step

- re-use the code from before:
- initialize a results variable to hld the result and set it to 0
- iterate over the digits in the string with no special chars
- with each iteration:
    - reassign the result to the sresult * 10--> this will shift the digit one place to make room for the next
    - add the result of subtracting the ASCCI value of 0 from that of the digit

lastly, if the original string had a negartive sign, multiply the resutl * -1 or return the result as is if there is another sign (the + sign)
"""


def string_to_signed_integer(str):
    no_sign_str = re.sub("\D","", str)

    result = 0
    for digit in no_sign_str:
        result = result * 10 + (ord(digit) - ord('0'))

    if str[0] == '-':
        return result * -1
    else:
        return result

print(string_to_signed_integer("4321") == 4321)  # True
print(string_to_signed_integer("-570") == -570)  # True
print(string_to_signed_integer("+100") == 100)   # True