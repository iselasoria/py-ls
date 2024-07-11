"""
You have a function that is supposed to
reverse a string passed as an argument.
However, it's not producing the expected
output. Explain the bug, and provide a solution.
"""
# OLD CODE

# def reverse_string(string):
#     for char in string:
#         string = char + string

#     return string

def reverse_string(string):
    rev = ''
    for char in string:
        rev = char + rev
    return rev

print(reverse_string("hello"))# == "olleh")