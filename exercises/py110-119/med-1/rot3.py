"""
Take the number 735291 and rotate it by one digit to the left,
getting 352917. Next, keep the first digit fixed in place and
rotate the remaining digits to get 329175. Keep the first two
digits fixed in place and rotate again to get 321759. Keep the
first three digits fixed in place and rotate again to get 321597.
Finally, keep the first four digits fixed in place and rotate
the final two digits to get 321579. The resulting number is
called the maximum rotation of the original number.

Write a function that takes an integer as an argument and returns
the maximum rotation of that integer. You can (and probably should)
use the rotate_rightmost_digits function from the previous exercise.


I: int
O: int

Rules:
- rotate the first digit to the left using the first function in this series


Model Solution:
- 735291
  *-----^
  352917
   *----^
  329175
    *---^
  321759
     *--^
  321597
      *-^
  321579

- There is a moving index or counter that becomes the slice size that keeps decreasing

DS:
- strings
- lists

Algo:
- cast integer to string
- init a result var to stringy num (used in the first iteration, reassigned thereafer)

- start a range of the length but backwards and iterate over it
    - with each iteration
        - call rotate_rightmost_digits() on the number and reassign result to this
            * now we're acting on each new rotation!! not on the original srtingy_num



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

def max_rotation(num):
    stringy_num = str(num)
    ongoing_rot = stringy_num

    for i in range(len(stringy_num), 0, -1):
        ongoing_rot = rotate_rightmost_digits(ongoing_rot, i)
        # print(ongoing_rot)

    return ongoing_rot

print(max_rotation(735291) == 321579)          # True
print(max_rotation(3) == 3)                    # True
print(max_rotation(35) == 53)                  # True
print(max_rotation(8703529146) == 7321609845)  # True

# # Note that the final sequence here is `015`. The leading
# # zero gets dropped, though, since we're working with
# # an integer.
print(max_rotation(105) == 15)                 # True