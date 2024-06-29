
"""
Given the following data structure, return a new list identical
in structure to the original but, with each number incremented by 1.
Do not modify the original data structure. Use a comprehension.
"""
lst = [{'a': 1}, {'b': 2, 'c': 3}, {'d': 4, 'e': 5, 'f': 6}]

# using for loops
# for d in lst:
#     for k, v in d.items():
#         # print(f'{k} and {v}')
#         d[k] = v + 1
# print(lst)

# using comprehensions
def increaser(dictionary):
    return {k: v + 1 for k, v in dictionary.items()}

new_list = [increaser(item) for item in lst]
print(new_list)

## coombining the two comprehensions into one
new_list = [{key: value + 1 for key, value in dictionary.items()}
                            for dictionary in lst]
# expected
[{'a': 2}, {'b': 3, 'c': 4}, {'d': 5, 'e': 6, 'f': 7}]

# ! TODO pattern is emerging here, when it's too complex you can delegate some work to a helper function like the sorting, or in this case the incrementation and then use another list coprehension to execute the actual transofrmation
