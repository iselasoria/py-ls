"""
Given the following data structure, sort the list so that the sub-lists are
ordered based on the sum of the odd numbers that they contain.
You shouldn't mutate the original list.
"""

lst = [[1, 6, 7], [1, 5, 3], [1, 8, 3]]

"""
Note that the first sublist has the odd numbers 1 and 7; the second sublist has
odd numbers 1, 5, and 3; and the third sublist has 1 and 3.
Since (1 + 3) < (1 + 7) < (1 + 5 + 3), the sorted list should look like this:
"""
[[1, 8, 3], [1, 6, 7], [1, 5, 3]]

def sum_of_odds(sublist):
    lista_de_nones = [num for num in sublist if num % 2 != 0]
    return sum(lista_de_nones)

sorted_list = sorted(lst, key=sum_of_odds)
print(sorted_list)

#! TODO revise this structure, maybe chunk it