"""
Write a function that takes a string, doubles every
character in the string, then returns the result as a new string.

I: string
O: string

Rules:
- double each character
    - keep the case as is

Model Solution:
Hello --> HHeelloo

DS:
Interim: list


Algo:
- initialize a string object `double_str`
- iterate over the chars of the argument string
    - with each iteration multiply the char by 2 and append
- return the `doble_str` joined with no space
"""
def repeater(str):
    double_str = [(ch*2) for ch in str]
    return ''.join(double_str)

# test cases
print(repeater('Hello') == "HHeelllloo")              # True
print(repeater('Good job!') == "GGoooodd  jjoobb!!")  # True
print(repeater('') == "")                             # True