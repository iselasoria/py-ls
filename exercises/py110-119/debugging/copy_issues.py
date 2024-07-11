"""
We have a list of lists and want to duplicate it. After making the copy,
we modify the original list, but the copied list also seems to be affected:
"""

# import copy

# original = [[1], [2], [3]]
# copied = copy.copy(original)

# original[0][0] = 99

# print(copied[0] == [1])

# SOLUTION
# the `.copy()` method makes a shallow copy, and in shallow copies nested elements inside a collection
# are shared, so when we use indexed reassignment to modify the first element of the first element, we are acting on the
# original object. We can make a deep copy instead and in deep capies, nested elements are not shared.

import copy

original = [[1], [2], [3]]
copied = copy.deepcopy(original)

original[0][0] = 99

print(copied[0] == [1])