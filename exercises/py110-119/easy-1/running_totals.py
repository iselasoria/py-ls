"""
Write a function that takes a list of numbers and returns a
list with the same number of elements, but with each element's
value being the running total from the original list.

Algo:
- initialize an empty list object
- iterate over the list while the length of the new list is less than the original length
- with each iteration
    - when index is 0, push the current element
    - push new list sum + current element

"""

def running_total(lst):
    new_list = []

    for idx, item in enumerate(lst):
        if idx == 0:
            new_list.append(item)
        else:
            # print(item)
            # print(new_list[-1])
            new_list.append(new_list[-1] + item)
    return new_list

print(running_total([2, 5, 13])== [2, 7, 20])    # True
print(running_total([14, 11, 7, 15, 20]) == [14, 25, 32, 47, 67])                    # True
print(running_total([3]) == [3])                  # True
print(running_total([]) == [])                    # True