"""
Modify the function from the previous exercise so it ignores non-alphabetic
characters when determining whether it should uppercase or lowercase each
letter. The non-alphabetic characters should still be included in the
return value; they just don't count when toggling the desired case.


Algo:
- init staggered_str
- init case_toggle to True


- iterate over the chars in the string
    - if the character is a letter and character toggle is true,
        - downcase and append to staggered_str
        - toggle becomes False
    - otherwise if the char is a letter and toggle is False
        - upcase and append to staggered_str
        - toggle becomes True
    - otherwise if the char is not alphabetic
        - append to staggered_str as is

- return staggared_str

"""

def staggered_case(str):
    staggered_str = ''
    case_toggle = True

    for char in str:
        if char.isalpha() and case_toggle:
            staggered_str += char.upper()
            case_toggle = not case_toggle
        elif char.isalpha() and case_toggle is False:
            staggered_str+= char.lower()
            case_toggle = not case_toggle
        else:
            staggered_str += char

    return staggered_str


string = 'I Love Launch School!'
result = "I lOvE lAuNcH sChOoL!"
print(staggered_case(string)== result)  # True

string = 'ALL_CAPS'
result = "AlL_cApS"
print(staggered_case(string) == result)  # True

string = 'ignore 77 the 4444 numbers'
result = "IgNoRe 77 ThE 4444 nUmBeRs"
print(staggered_case(string) == result)  # True

print(staggered_case('') == "")          # True