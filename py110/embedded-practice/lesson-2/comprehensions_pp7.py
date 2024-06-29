"""
Given the following data structure return a new list identical
in structure to the original,
but containing only the numbers that are multiples of 3.
"""

lst = [[2], [3, 5, 7, 12], [9], [11, 15, 18]]

# using for loops
new_list = []

for tiny_list in lst:
    mini_list = []
    for num in tiny_list:
        if num % 3 == 0:
            mini_list.append(num)
    new_list.append(mini_list)
(print('This was done with loops: '))
print(new_list)


# refactored
new_list = []

for tiny_list in lst:
    mini_list = [num for num in tiny_list if num % 3 == 0]
    new_list.append(mini_list)
print('This was done with one list comprehension')
print(new_list)

# refactor the comprehensions above into a helper function
def multiples_of_three(tiny_list):
    return [num for num in tiny_list if num % 3 == 0]

new_list = [multiples_of_three(tiny_list) for tiny_list in lst]
print('This was done with multiple comprehensions and a helper function: ')
print(new_list)

# comprehension eleganza
new_list = [[num for num in sublist if num % 3 == 0] for sublist in lst]
print('Now we\'re just showing off here: ')
print(new_list)

# expected result
[[], [3, 12], [9], [15, 18]]

# ! TODO revise; this could be the chunk!!!!
