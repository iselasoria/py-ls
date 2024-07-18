"""
Write a function that takes a string of digits and returns the appropriate
number as an integer. You may not use any of the standard conversion functions
available in Python, such as int. Your function should calculate the result
by using the characters in the string.

For now, do not worry about leading + or - signs, nor should you worry about
invalid characters; assume all characters are numeric.

I: string
O: integer

Examples:
    "4321" --> 4321
len: 4
    4000
     300
      20
       1

DS:
I: str
Interim: list/dict
O: int

Algo:
- initalize `result` to int 0
- initialize `equivalents` dict with str and int equivalents
- iterate over the input str
    - with each iteration
        - multiply the current by 10

If you call string_to_integer("123"), here's what happens step-by-step:

Initially, result is 0.
For each character (digit) in "123":
result is multiplied by 10.
For each d in '0123456789':
For '1': '1' > '0' is True, so result becomes 1.
For '2': '2' > '0' and '2' > '1' are both True, so result becomes 12.
For '3': '3' > '0', '3' > '1', and '3' > '2' are all True, so result becomes 123.


"""

#? review algo

# def string_to_integer(str):
#     result = 0

#     for digit in str:
#         result *= 10
#         # print(result)
#         for d in '0123456789':
#             result += digit > d

#     return result


def string_to_integer(str):
    result = 0
    for digit in str:
        result = result * 10 + (ord(digit) - ord('0'))
    return result



# test cases
print(string_to_integer("4321"))# == 4321)  # True
print(string_to_integer("570") )#== 570)    # True
print(string_to_integer("57"))# == 570)    # True