
## Problem:
Given a list of strings, return a new list where the strings are sorted based on the highest number of adjacent consonants a string contains. If two strings contain the same highest number of adjacent consonants, they should retain their original order in relation to each other. Consonants are considered adjacent if they are next to each other in the same word or if there is a space between two consonants in adjacent words.


## I: list of strings
## O: new list

## Rules:
- adjacent consonants
    - consonants next to eachother
    - consonants separated by a space
    - if two strings tie, retain the order of the original list

## Examples:
```python
my_list = ['aa', 'baa', 'ccaa', 'dddaa']
print(sort_by_consonant_count(my_list))
# ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

my_list = ['bar', 'car', 'far', 'jar']
print(sort_by_consonant_count(my_list))
# ['bar', 'car', 'far', 'jar']

my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']

my_list = ['xxxa', 'xxxx', 'xxxb']
print(sort_by_consonant_count(my_list))
# ['xxxx', 'xxxb', 'xxxa']
```

-


## Model Solution:
my_list = ['day', 'week', 'month', 'year']
print(sort_by_consonant_count(my_list))
# ['month', 'day', 'week', 'year']


## DS:
Intermediate Data Structure: Dictionary

## Algo:
- initialize an empty dictionary `consonant_tally`
- iterate over the input list
- with every iteration
    - initialize a string object `adj_cons_in_word`
    - iterate over the string characters
        - push character to `adj_cons_in_word` IF the last char in the variable is also consonant
    - write to the `consonant_tally`
        - word as key
        - the length of `adj_cons_in_word` as value


