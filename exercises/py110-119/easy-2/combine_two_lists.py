"""
Write a function that combines two lists passed as arguments and returns a new list that
contains all elements from both list arguments, with each element taken in alternation.

You may assume that both input lists are non-empty, and that they have the same number of elements.


I: two lists
O: list

Rules:
- alternating elements from each list

DS:
- lists

Algo:
- initialize a results list
- zip lists
- iterate over pairs
    - dump each item in results list
- return results list
"""


def interleave(lst1, lst2):
    results = []
    zippy = zip(lst1, lst2)

    for pair in zippy:
        for item in pair:
            results.append(item)

    return results

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
expected = [1, "a", 2, "b", 3, "c"]
print(interleave(list1, list2) == expected)      # True