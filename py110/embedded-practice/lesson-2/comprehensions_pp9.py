"""
This problem may prove challenging. Try it, but don't stress about it.
If you don't solve it in 20 minutes, you can look at the answer.

Given the following data structure, write some code to return
a list that contains only the dictionaries where all the numbers are even.

I: list
O: list

Rules:
- selecting only dictionaries where all the numbers in the keys are even


DS:
I: list
Interim: dictionary
O: list

Algo:

- iterate over the list
- with each iteration
    - access the values--> lists
        - filter if all the numbers int he list are even



"""

lst = [
    {'a': [1, 2, 3]},
    {'b': [2, 4, 6], 'c': [3, 6], 'd': [4]},
    {'e': [8], 'f': [6, 10]},
]

def only_even(dictionary):
    for v in dictionary.values():
        if not all([num % 2 == 0 for num in v]):
            return False

    return True

result = [tiny_dict for tiny_dict in lst if only_even(tiny_dict)]
print(result)
# expected
[{'e': [8], 'f': [6, 10]}]

#! TODO review this