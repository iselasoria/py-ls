"""
Write a function that takes a string, doubles every consonant
in the string, and returns the result as a new string.
The function should not double vowels ('a','e','i','o','u'),
digits, punctuation, or whitespace.

You may assume that only ASCII characters will be included
in the argument.


I: string
O: string

Rules
- double only consonats
- leave vowels untouched
- keep case
- digits are allowed and should be left alone just like vowels

Model Soultion:
- String --> SSttrrinngg
- July 4th --> JJullyy 4tthh"

DS:
interim: list

Algo:
- iterate over the input string characters
- with each iteration
    - if the character is not found in vowels, double it then append it
    - if it is, append it

- join and return the new collection


"""

def double_consonants(str):
    transformed_list = []

    for ch in str:
        if ch not in 'AEIOUaeoiu- 4!':
            transformed_list.append((ch * 2))
        else:
            transformed_list.append(ch)
    return ''.join(transformed_list)
# test cases
# All of these examples should print True
print(double_consonants('String')== "SSttrrinngg")
print(double_consonants('Hello-World!') == "HHellllo-WWorrlldd!")
print(double_consonants('July 4th') == "JJullyy 4tthh")
print(double_consonants('') == "")