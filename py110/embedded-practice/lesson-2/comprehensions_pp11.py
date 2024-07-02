"""
The following dictionary has list values that contains strings.
Write some code to create a list of every vowel (a, e, i, o, u)
that appears in the contained strings, then print it.


Start by trying to write this using nested loops.

Extra Challenge: Once your nested loop code works, try to refactor the
code so it uses a single list comprehension.
(You can print the resulting list outside of the comprehension.)

"""

dict1 = {
    'first':  ['the', 'quick'],
    'second': ['brown', 'fox'],
    'third':  ['jumped'],
    'fourth': ['over', 'the', 'lazy', 'dog'],
}

# Using nested loops
vowels = []

for item in dict1:
    for dict_val in dict1[item]:
        for ch in dict_val:
            if ch in 'AEIOUaeiou':
                vowels.append(ch)
print(vowels)

# Using list comprehensions
vowels = 'aeiou'

chars = [char for key in dict1
            for word in dict1[key]
            for char in word if char in vowels]
print(chars)
# print(list_of_vowels)
# ['e', 'u', 'i', 'o', 'o', 'u', 'e', 'o', 'e', 'e', 'a', 'o']
#! DONE revise list comprehensions