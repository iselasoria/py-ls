"""
Write a function that takes a string as an argument and returns that
string with every occurrence of a "number word" -- 'zero', 'one', 'two',
'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' -- converted
to its corresponding digit character.

You may assume that the string does not contain any punctuation.

I: str
O: str

Rules:
- take a string and extract the digits that are spelled out
- assume no punctuation

DS:
string

Algo:
- init a dict of numbers 0-9 and their engish words as keys
- split the input string
- init result to []

- iterate over split string (now a list)
    - with each iteration
        - if the key exists in the dict, retrieve value and push as a string to result
        - otherwise just push as is
- join result string with spaces and return
"""

def word_to_digit(msg):
    msg_lst = msg.split()
    numberpad = {'zero': 0, 'one':1, 'two': 2,
                 'three': 3, 'four': 4, 'five': 5,
                 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    result = []

    for word in msg_lst:
        if word in numberpad:
            result.append(str(numberpad.get(word)))
        else:
            result.append(word)

    return ' '.join(result)

message = 'Please call me at five five five one two three four'
print(word_to_digit(message) == "Please call me at 5 5 5 1 2 3 4")
# Should print True