"""
We want to create a function that appends a given value to a list. However,
the function seems to be behaving unexpectedly:
"""

# def append_to_list(value, lst=[]):
#     lst.append(value)
#     return lst

def append_to_list(value, lst=None):
    if lst is None:
        lst = []

    lst.append(value)
    return lst


print(append_to_list(1) == [1])
print(append_to_list(2) == [2])

# SOLUTION
# in Python, defeault mutable arguments are shared amongst funcrtion calls.
# this means that if you modify the default argument, its state will persist across
# other function calls as well