"""
In the previous two exercises, you developed functions that
convert simple numeric strings to signed integers. In this
exercise and the next, you're going to reverse those functions.
Write a function that converts a non-negative integer value
(e.g., 0, 1, 2, 3, and so on) to the string representation of
that integer.

You may not use any of the standard conversion functions
available in Python, such as str. Your function should do
this the old-fashioned way and construct the string by
analyzing and manipulating the number.
"""

def integer_to_string(num):
    digits = num / 10000
    print(digits)

print(integer_to_string(4321))# == "4321")              # True
# print(integer_to_string(0) == "0")                    # True
# print(integer_to_string(5000) == "5000")              # True
print(integer_to_string(1234567890) )#== "1234567890")  # True