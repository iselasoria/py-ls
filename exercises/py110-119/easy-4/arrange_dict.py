# Given a dictionary, return its keys sorted by the values associated with each key.

"""
- Grab the key/val pairs
    - dict.items() --> [key, val] --> item[1] will give us the value
    - this becomes the helper function
- The main function sorts the keys by the values so we can use .items to retrieve the k/v pairs
    and then use the helper fucntion to sort on the values
    - return only the key in this newly sorted dictionary
"""


def sort_me(item):
    return my_dict[item]

def order_by_value(d):
    my_dict.values().sort()

my_dict = {'p': 8, 'q': 2, 'r': 6}
keys = ['q', 'r', 'p']
print(order_by_value(my_dict) == keys)  # True