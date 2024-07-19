"""
Write a function that takes a list of strings and returns a list of the same
string values, but with all vowels (a, e, i, o, u) removed.

I: list
O: list

Rules:
- take a list of strings and return a las of the same string vals
- remove all vowels

DS:
- list

Algo:
- iterate over input list
    - initialize element strinng ''

    - for each element --> 'abcdefdhi'
        - if its a vowel, skip
        - if not append to element string
- return the list


"""

def remove_vowels(lista):
    mother_list = []

    for item in lista:
        element_str = ''
        for ch in item:
            if ch in 'AEOIUaeiou':
                continue
            else:
                element_str += ch
        mother_list.append(element_str)

    return mother_list
# All of these examples should print True
original = ['abcdefghijklmnopqrstuvwxyz']
expected = ['bcdfghjklmnpqrstvwxyz']
print(remove_vowels(original) == expected)        # True

original = ['green', 'YELLOW', 'black', 'white']
expected = ['grn', 'YLLW', 'blck', 'wht']
print(remove_vowels(original)== expected)        # True

original = ['ABC', 'AEIOU', 'XYZ']
expected = ['BC', '', 'XYZ']
print(remove_vowels(original) == expected)        # True