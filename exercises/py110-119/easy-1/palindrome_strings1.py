"""
Write a function that returns True if the string passed as an
argument is a palindrome, False otherwise. A palindrome reads
the same forwards and backwards. For this problem,
the case matters and all characters matter.

I: string
O: Boolean

Rules:
- Return True of input is palindrome
    - spelled same forward and backward
    - all characters matter
    - case matters--> don't casefold!!

Examples/Model Solution:
'madam'
'356653

DS:
I: string
Interim: list
O: bool

Algo:
- initialize a variable to hold a list equivalent of the string
- reverse the list above
- join it back to a string and store in a new variable
- return the validity of string as compared to the reversed string
"""

def is_palindrome(string):
    str_to_lst = list(string)
    str_to_lst.reverse()
    string_rev = ''.join(str_to_lst)

    return string == string_rev



# test cases
# All of these examples should print True

print(is_palindrome('madam') == True)
print(is_palindrome('356653') == True)
print(is_palindrome('356635') == False)
# # case matters
print(is_palindrome('Madam') == False)
# all characters matter
print(is_palindrome("madam i'm adam") == False)