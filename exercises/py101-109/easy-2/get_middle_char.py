"""
Write a function that takes a non-empty string argument and returns the middle
character(s) of the string. If the string has an odd length, you should
return exactly one character. If the string has an even length, you
should return exactly two characters.

I:
str

O: str

Algo:
- determine len of string
- determine half
- if odd, return character at index where the half value is
- if even, return a slice half - 1 for a length of two
"""


# def center_of(str):
#     size = len(str)
#     half = size // 2

#     if size % 2 == 0:
#         return str[half - 1 : half + 1]
#     else:
#         return str[half]


def center_of(str):
    size = len(str)
    half = len(str) // 2

    return str[half - 1 : half + 1] if size & 1 == 0 else str[half]

# test cases
print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True
