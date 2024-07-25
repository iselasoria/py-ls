"""
Write a function that rotates a list by moving the first element to the end of the list. Do not modify the original list; return a new list instead.

If the input is an empty list, return an empty list.
If the input is not a list, return None.
Review the test cases below, then implement the solution accordingly.

----------------------------------
Write a function that rotates the last count digits of a number. To perform the rotation, move the first of the digits that you want to rotate to the end and shift the remaining digits to the left.

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True

----------------------------------

I: int, int
O: int

Rules:
- first input int is a number with digits and the second is the number of digits to rotate

Model Solution:
inputs: 735291, 2
            --
result: 735219

input: 735291, 3
          ---
          *--^
result:735912

input:  735291, 4
          ----
          *---^
result: 732915

DS:
interim: string, lists

Algo:
- convert input1 as string to list --> 735291 --> "735291" --> ['7','3','5','2','9','1'] stored in `num_list`
- slice from neg index slice_size to the end of the list `slice` --> ['9','1']
- call rotate_list() on slice and store in `rotated_slice` --> ['1','9']
- append num_list from 0 to negative input2 to rotated_slice --> ['7'','3','5','1','9']
- join the list w/o spaces and cast as int and return

"""
def rotate_list(lst):
    if not type(lst) == list:
        return None
    if len(lst) == 0:
        return []


    lst_cp = lst.copy()
    former_first = lst_cp.pop(0)
    lst_cp.append(former_first)

    return lst_cp

def rotate_rightmost_digits(number, slice_size):
    num_list = list(str(number))
    slice_ = num_list[-slice_size:]
    # print(slice_)

    rotated_slice = rotate_list(slice_)
    # print(rotated_slice)
    first_slice = num_list[:-slice_size]
    first_slice.extend(rotated_slice)

    return int(''.join(first_slice))


# print(rotate_rightmost_digits(735291, 2))

print(rotate_rightmost_digits(735291, 2) == 735219)  # True
print(rotate_rightmost_digits(735291, 3) == 735912)  # True
print(rotate_rightmost_digits(735291, 1) == 735291)  # True
print(rotate_rightmost_digits(735291, 4) == 732915)  # True
print(rotate_rightmost_digits(735291, 5) == 752913)  # True
print(rotate_rightmost_digits(735291, 6) == 352917)  # True
print(rotate_rightmost_digits(1200, 3) == 1002)      # True