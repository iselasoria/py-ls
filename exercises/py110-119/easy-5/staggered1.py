"""
Write a function that takes a string as an argument and returns that
string with a staggered capitalization scheme. Every
other character, starting from the first, should be
capitalized and should be followed by a lowercase or
non-alphabetic character. Non-alphabetic characters
should not be changed, but should be counted as
characters for determining when to switch between upper
and lower case.

I: string
O: string

Rules:
- alternate by index the case of the character
    - punctuation does not change the index reference point for determining case
- implicit: start with uppercase

Model Solution:
I Love Launch School!
01234567891011121314151617181920
I LoVe lAuNcH ScHoOl! -----> even index gets capitalized

DS:
lists

Algo:
- init staggered_str

- iterate over the chars and their idx
    - if the index is even, upcase the char and add to staggered_str
    - otherwise lowercase the char and add to staggered_str
- return staggered_str

"""

def staggered_case(str):
    staggered_str = ''

    for idx, char in enumerate(str):
        if idx % 2 == 0:
            staggered_str += char.upper()
        else:
            staggered_str += char.lower()

    return staggered_str


string = 'I Love Launch School!'
result = "I LoVe lAuNcH ScHoOl!"
print(staggered_case(string) == result)  # True

string = 'ALL_CAPS'
result = "AlL_CaPs"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True