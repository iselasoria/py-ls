"""
Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.

I: list
O: (new) list

Rules:
- move the first element to the end
- don't modify the original

Model Solution:
original: [7, 3, 5, 2, 9, 1]
index:     0  1. 2. 3  4. 5
result :  [3, 5, 2, 9, 1, 7]
new_idx:   1, 2  3. 4  5  0

DS:
lists

Algo:
- if empty list return empty list
- if input arg is not of the type list, return None
- make a shallow copy of input list `lst_cp`
- remove the first element and store in `former_first` [3,5,2,9,1] --> 7
- append `former_first` to the `lst_cp`  and return


"""

def rotate_list(lst):
    if not type(lst) == list:
        return None
    if len(lst) == 0:
        return []


    lst_cp = lst.copy()
    former_first = lst_cp.pop(0) #7
    lst_cp.append(former_first)
    return lst_cp



# All of these examples should print True

print(rotate_list([7, 3, 5, 2, 9, 1]) == [3, 5, 2, 9, 1, 7])
print(rotate_list(['a', 'b', 'c']) == ['b', 'c', 'a'])
print(rotate_list(['a']) == ['a'])
print(rotate_list([1, 'a', 3, 'c']) == ['a', 3, 'c', 1])
print(rotate_list([{'a': 2}, [1, 2], 3]) == [[1, 2], 3, {'a': 2}])
print(rotate_list([]) == [])

# return `None` if the argument is not a list
print(rotate_list(None)== None)
print(rotate_list(1) == None)

# the input list is not mutated
lst = [1, 2, 3, 4]
print(rotate_list(lst) == [2, 3, 4, 1])
print(lst == [1, 2, 3, 4])