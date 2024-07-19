"""
Given a dictionary and a list of keys, produce a new dictionary that only
contains the key/value pairs for the specified keys.

I: dict, list
O: dict

Rules:
- only keep the k/v pairs that match the specified key in the input list

- select only elements whose keys are in the keys dicitonary


"""

def keep_keys(input_d, keys_to_match):
    return {k : v for k, v in input_d.items() if k in keys_to_match}


input_dict = {
    'red': 1,
    'green': 2,
    'blue': 3,
    'yellow': 4,
}

keys = ['red', 'blue']
expected_dict = {'red': 1, 'blue': 3}
print(keep_keys(input_dict, keys) == expected_dict) # True

