"""
Given the following data structure, write some code that defines a
dictionary where the key is the first item in each sublist, and
the value is the second.
"""

lst = [
    ['a', 1],
    ['b', 'two'],
    ['sea', {'c': 3}],
    ['D', ['a', 'b', 'c']]
]

# expected

# Pretty printed for clarity
# {
#     a: 1,
#     b: 'two',
#     sea: {c: 3},
#     D: ['a', 'b', 'c']
# }

this_dictionary = {tiny_lst[0]: tiny_lst[1] for tiny_lst in lst}

print(this_dictionary)