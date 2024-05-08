"""
Write a function that takes one argument, a positive integer, and
returns a string of alternating '1's and '0's, always starting with a '1'.
The length of the string should match the given integer.

I:
positive int

O:
string

Rules:
- resulting string is the same length as the integer number
- alternating 1s and 01
- slways start with 1

Algo:
- initialize an empty list
- iterate over the lenght of 0 to the integer as the top threshold
- with each iteration
    - if the number of the iteration is even, place a 1
    - otherwise place a 0

- join the list owth no spaces and return the new string

"""
# ! TODO can this be further cleaned into a list comprehension?

# def stringy(num):
#     soon_tobe_str = []

#     for idx in range(num):
#         if idx & 1 == 0:
#             soon_tobe_str.append('1')
#         else:
#             soon_tobe_str.append('0')

#     return ''.join(soon_tobe_str)

def stringy(num):

    return''.join(['1' if idx & 1 == 0 else '0' for idx in range(num)])

print(stringy(6) == "101010")          # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
