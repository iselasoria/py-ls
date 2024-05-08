"""
Write a function that takes a string argument and returns a
new string that contains the value of the original string with
all consecutive duplicate characters collapsed into a single character.

I:
string

O:
string

Algo:
- initialize an empty list
- iterate over the characters in the string
    - if the characrter is the list element in the list, next
    - if it does not, add it to the empty list
- join the list into a string and return

"""

# ! TODO review and clean this up into a more Pythonic solution
def crunch(str):
    compact = []

    for char in range(len(str) - 1):
        if char == str[-1]:
            compact.append(str[char])
        elif str[char] == str[char + 1] and char != str[-1]:
            pass
        else:
            compact.append(str[char])
    compact.append(str[-1])

    return ''.join(compact)

# These examples should all print True
print(crunch('ddaaiillyy ddoouubbllee')) #== 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')