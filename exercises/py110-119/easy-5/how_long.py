"""
Write a function that takes a string as an argument and returns a list that
contains every word from the string, with each word followed by a space and
the word's length. If the argument is an empty string or if no argument is
passed, the function should return an empty list.

You may assume that every pair of words in the string will be separated by
a single space.


I: string
O: list

Rules:
- returns list of strings
- each element is a string that contains the word and its leght
- empty strings as input will return an emprt array

DS:
- lists

Algo:
- if string is empty, return emprt list

- split the string at the space split_str
- for each elment in the split_str
    - transform into word + length of word

"""
def word_lengths(words=''):
    if not words:
        return []

    split_str = words.split()
    return [item + ' ' + str(len(item)) for item in split_str]


# All of these examples should print True
words = 'cow sheep chicken'
expected_result = ['cow 3', 'sheep 5', 'chicken 7']
print(word_lengths(words) == expected_result)        # True

words = 'baseball hot dogs and apple pie'
expected_result = ['baseball 8', 'hot 3', 'dogs 4',
                   'and 3', 'apple 5', 'pie 3']
print(word_lengths(words) == expected_result)        # True

words = "It ain't easy, is it?"
expected_result = ['It 2', "ain't 5", 'easy, 5',
                   'is 2', 'it? 3']
print(word_lengths(words) == expected_result)        # True

big_word = 'Supercalifragilisticexpialidocious'
print(word_lengths(big_word) == [f'{big_word} 34'])  # True

print(word_lengths('') == [])                        # True
print(word_lengths() == [])                          # True