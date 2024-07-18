"""
Write a function that returns a list of all palindromic substrings of a string.
That is, each substring must consist of a sequence of
characters that reads the same forward and backward. The substrings in the
returned list should be sorted by their order of appearance
in the input string. Duplicate substrings should be included multiple times.

You may (and should) use the substrings function you wrote in the previous exercise.

For the purpose of this exercise, you should consider all characters
and pay attention to case; that is, 'AbcbA' is a palindrome,
but 'Abcba' and 'Abc-bA' are not. In addition, assume that single characters are not palindromes.
"""
def is_palin(str):
    return str == str[::-1]

def palindromes(str):
    substrings = []

    for start_idx in range(len(str)):
        for end_idx in range(len(str)):
            suby = str[start_idx:end_idx + 1]
            if is_palin(suby) and len(suby) > 1:
                substrings.append(suby)
    return substrings


print(palindromes('abcd')== [])                  # True
print(palindromes('madam') == ['madam', 'ada'])   # True

print(palindromes('hello-madam-did-madam-goodbye') ==
                  [
                      'll', '-madam-', '-madam-did-madam-',
                      'madam', 'madam-did-madam', 'ada',
                      'adam-did-mada', 'dam-did-mad',
                      'am-did-ma', 'm-did-m', '-did-',
                      'did', '-madam-', 'madam', 'ada', 'oo',
                  ])    # True

print(palindromes('knitting cassettes') ==
                  [
                      'nittin', 'itti', 'tt', 'ss',
                      'settes', 'ette', 'tt',
                  ])    # True