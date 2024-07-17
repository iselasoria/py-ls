"""
Write a function that takes a list as an argument and reverses its elements, in place.
That is, mutate the list passed into the function. The returned object should be the
same object used as the argument.

You may not use the list.reverse method nor may you use a slice ([::-1]).

I: list
O: same list

Rules:
- must mutate in place
- reverse the list
- cannot use `reverse()`
- cannot use slice [::-1]

Model Soltion:
lst = [1, 2, 3, 4]
lst[0] = lst[-1]
lst[1] = lst[-2]

DS:
Interim:
list

Algo:
initialize downward_tracker to the length of the list

- iterate over the list up to half because by that point we will have swapped all
    - for each iteration
        - reassign the element at the current index to the element of the downward tracker
        - reduce the tracker by 1
    - return the list object

"""

def reverse_list(lst):
    downward_tracker = len(lst)

    for idx in range(downward_tracker // 2):
        lst[idx], lst[-(idx + 1) ]= lst[-(idx + 1)], lst[idx]
        downward_tracker -= 1
    return lst

# test cases
list1 = [1, 2, 3, 4]
result = reverse_list(list1)
print(result == [4, 3, 2, 1])               # True
print(list1 is result)                      # True

list2 = ["a", "b", "c", "d", "e"]
result2 = reverse_list(list2)
print(result2 == ['e', 'd', 'c', 'b', 'a']) # True
print(list2 is result2)                     # True

list3 = ["abc"]
result3 = reverse_list(list3)
print(result3 == ['abc'])                   # True
print(list3 is result3)                     # True

list4 = []
result4 = reverse_list(list4)
print(result4 == [])                        # True
print(list4 is result4)                     # True