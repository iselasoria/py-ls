"""
You have a function that should check whether a key exists in a dictionary and
returns its value. However, it's raising an error. Why is that?
How would you fix this code?
"""

# def get_key_value(my_dict, key):
#     if my_dict[key]:
#         return my_dict[key]
#     else:
#         return None

# print(get_key_value({"a": 1}, "b"))

# SOLUTION
# attempting to use a key that doesn't exist results in an error. We could use `.get()`
# to check that they key exists before we attempt to access it

# def get_key_value(my_dict, key):
#     if my_dict.get(key):
#         return my_dict[key]
#     else:
#         return None

# cleaner code
def get_key_value(my_dict, key):
    return my_dict.get(key, None)

print(get_key_value({"a": 1}, "b"))
