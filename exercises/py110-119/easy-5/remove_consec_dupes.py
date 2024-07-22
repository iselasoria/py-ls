"""
Given a sequence of integers, filter out instances where the same value
occurs successively, retaining only the initial occurrence. Return the
refined sequence.


I: list
O: list

Rules:
- remove instances where the same val occurs successively
- result is the refined sequence

Algo:
- init new list

- iterate over the list
    - for each iteration
        - append the number to the list if the new list's last number is not the same as current
- return new_list


"""

def unique_sequence(col):
    new_lst = []
    new_lst.append(col[0])

    for num in col[1:]:
        if new_lst[-1] != num:
            new_lst.append(num)

    return new_lst

original = [1, 1, 2, 6, 6, 6, 5, 5, 3, 3, 3, 4]
expected = [1, 2, 6, 5, 3, 4]
print(unique_sequence(original) == expected)      # True