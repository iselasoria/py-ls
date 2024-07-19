"""
Write a function that takes a list of numbers and
returns the sum of the sums of each leading subsequence
in that list. Examine the examples to see what we mean.
You may assume that the list always contains at least
one number

I: list
O: int

Rules:
- return sum of each "sub chunk" of the list
- assume the list will contain at least one element

Model Solution:
print(sum_of_sums([3, 5, 2]) == 21)
        (3) + (3 + 5) + (3 + 5 + 2)
        (3) + (8) + (10)
        21


DS:
lists

Algo:
- iterate over the input list from index 0 to end of range
    - for a slice of the list from 0 up to the sliding index
        - sum the list and append to sumas list
- return the sum of the sumas list

"""
def sum_of_sums(lst):
    sumas = []

    for sliding_idx in range(len(lst)):
        slice = lst[:sliding_idx + 1]
        sumas.append(sum(slice))
    return sum(sumas)

print(sum_of_sums([3, 5, 2]) == 21)               # True
# (3) + (3 + 5) + (3 + 5 + 2) --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)            # True
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 36

print(sum_of_sums([1, 2, 3, 4, 5]) == 35)         # True
# (1) + (1+2) + (1+2+3) + (1+2+3+4) + (1+2+3+4+5) --> 35

print(sum_of_sums([4]) == 4)                      # True