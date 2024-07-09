"""
Write a function that takes a list as an argument and returns a list that contains two elements,
both of which are lists. Put the first half of the original list elements in the first
element of the return value and put the second half in the second element. If the original
list contains an odd number of elements, place the middle element in the first half list.

I: list
O: nested list

Rules:
- first element should contain up to the half
- second element should contain from half to the end
- if original list is odd length, the middle element goes in the first element of the return list

Model Solution:
EVEN--
    [1,2,3,4]
len --> 4
middle --> 2
list at middle index --> 3; don't include middle in first half
lst[:middle]
[[1, 2], [3, 4]]

ODD--
    [1, 5, 2, 4, 3]
len --> 5
middle --> 2
list at middle index --> 2; do include in first half
lst[:middle + 1]
[[1, 5, 2], [4, 3]]


DS:
lists

Algo:
- find middle
- if odd length
    - slice from start to end + 1, slice from middle to end


- if even
    - slice

"""

def halvsies(lst):
    half = len(lst) // 2

    if len(lst) % 2 == 0:
        return [lst[:half], lst[half:]]
    else:
        return [lst[:half + 1], lst[half + 1:]]


# All of these examples should print True
print(halvsies([1, 2, 3, 4]) == [[1, 2], [3, 4]])
print(halvsies([1, 5, 2, 4, 3]) == [[1, 5, 2], [4, 3]])
print(halvsies([5]) == [[5], []])
print(halvsies([]) == [[], []])