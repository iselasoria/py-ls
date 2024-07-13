"""
Write another function that returns True if the string passed as an argument
is a palindrome, or False otherwise. This time, however, your
function should be case-insensitive, and should ignore all non-alphanumeric
characters. If you wish, you may simplify things by calling the
is_palindrome function you wrote in the previous exercise.
"""


def is_real_palindrome(string):
    clean_str = ''
    for ch in string:
        if ch.isalnum():
            clean_str += ch.casefold()

    str_to_lst = list(clean_str)
    str_to_lst.reverse()
    string_rev = ''.join(str_to_lst)

    return clean_str == string_rev

# test cases
print(is_real_palindrome('madam') == True)           # True
print(is_real_palindrome('356653') == True)          # True
print(is_real_palindrome('356635') == False)         # True
print(is_real_palindrome('356a653') == True)         # True
print(is_real_palindrome('123ab321') == False)       # True

# case doesn't matter
print(is_real_palindrome('Madam') == True)           # True

# only alphanumerics matter
print(is_real_palindrome("Madam, I'm Adam") == True) # True