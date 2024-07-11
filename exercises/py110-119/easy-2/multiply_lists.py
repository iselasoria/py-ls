"""
Write a function that takes two list arguments, each containing a list of numbers,
and returns a new list that contains the product of each pair of numbers
from the arguments that have the same index. You may assume that
the arguments contain the same number of elements.

I: list
O: list

Rules:
- multiply numbers from each list that have the same index
- safe to assume arguments have the same number of elements

Model Solution:
list_1 [3, 5, 7]
list_2 [9, 10, 11]
index   0  1   2
3 * 5, 5 * 10, 7 * 11
[15, 50, 77]

DS:
Interim: tuple

Algo:
- zip the two lists --> (item1_list1, item1_list2)
- iterate over the list of tuples
    - multiple tuple at 0 and tuple at 1
    - return in new list

"""

def multiply_list(lst1, lst2):
    zippy = list(zip(lst1, lst2))

    return [(pair[0] * pair[1]) for pair in zippy]


list1 = [3, 5, 7]
list2 = [9, 10, 11]
print(multiply_list(list1, list2))== [27, 50, 77])  # True