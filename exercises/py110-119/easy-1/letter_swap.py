"""
Given a string of words separated by spaces, write a function that
swaps the first and last letters of every word.

You may assume that every word contains at least one letter,
and that the string will always contain at least one word.
You may also assume that each string contains nothing but
words and spaces, and that there are no leading, trailing,
or repeated spaces.


I: string
O: string

Rules:
- string contains words separated by sapces
- result shouldbhave the first and last letters of the word, swapped
- assume no repeated spaces
- assume no sepecial characters


Examples/Model Solution:
'Oh what a wonderful day it is'
'hO thaw a lonferuw yad ti si'



DS:
I: string
Interim: list
O: string


Algo:
- initialize empty list `swapped`
- split the string into a list of words and store in `words`
- iterate over the list of words
- with every iteration, track index
    - make a list of the characters in the word and give list at 0, the value of list of -1 and vice versa.
    - join the list above back into string
    - use index reassignment to assign list at index to the item we just swapped
- return `swapped` joined by a space
"""

def swap(str):
    swapped = []
    words = str.split(' ')

    for word in words:
        w_list = list(word)
        w_list[0], w_list[-1] = w_list[-1], w_list[0]
        w_list = ''.join(w_list)
        swapped.append(w_list)

    return ' '.join(swapped)



# test cases
print(swap('Oh what a wonderful day it is') == "hO thaw a londerfuw yad ti si")  # True
print(swap('Abcde') == "ebcdA")            # True
print(swap('a') == "a")                    # True
