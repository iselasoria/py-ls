""""
Write a function that takes a string consisting of zero or more
space-separated words and returns a dictionary that shows
the number of words of different sizes.

Words consist of any sequence of non-space characters.

I: string
O: dictionary

Rules:
- count the number of words that have the same legnth
- string can be emprty, and if so it should return empty dictionary

Examples/Model Solution:
    Four score and seven.'
size: 4    5    3   6

result --> {size :  count} ==> {4: 1, 5: 1, 3: 1, 6: 1}


DS:
I: string
Interim: list
O: dict

Algo:
- initialize a dict object `ltr_counter`
- split input string at space

- iterate over the list
    - with every iteration
        - set the default to 0
        - if the length of the current word is the same as the counter, increase it

- return `ltr_counter`
"""

def word_sizes(str):
    if not str:
        return {}

    ltr_counter = {}
    words = str.split(' ')

    for word in words:
        ltr_counter.setdefault(len(word), 0)
        ltr_counter[len(word)] += 1

    return ltr_counter


# test cases
# All of these examples should print True

string = 'Four score and seven.'
print(word_sizes(string) == {4: 1, 5: 1, 3: 1, 6: 1})

string = 'Hey diddle diddle, the cat and the fiddle!'
print(word_sizes(string) == {3: 5, 6: 1, 7: 2})

string = 'Humpty Dumpty sat on a wall'
print(word_sizes(string) == {6: 2, 3: 1, 2: 1, 1: 1, 4: 1})

string = "What's up doc?"
print(word_sizes(string) == {6: 1, 2: 1, 4: 1})

print(word_sizes('') == {})