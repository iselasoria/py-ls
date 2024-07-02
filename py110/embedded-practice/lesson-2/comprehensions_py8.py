"""
Given the following data structure, write some code to return a
list that contains the colors of the fruits and the sizes of the vegetables.
The sizes should be uppercase, and the colors should be capitalized.

I: dicitonary
O: list

Model Solution:
{
'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    }
}

Algo:
- iterate over the dict
- with each iteration
    - if k is fruit, append colors
    - otherwise append size


"""

dict1 = {
    'grape': {
        'type': 'fruit',
        'colors': ['red', 'green'],
        'size': 'small',
    },
    'carrot': {
        'type': 'vegetable',
        'colors': ['orange'],
        'size': 'medium',
    },
    'apricot': {
        'type': 'fruit',
        'colors': ['orange'],
        'size': 'medium',
    },
    'marrow': {
        'type': 'vegetable',
        'colors': ['green'],
        'size': 'large',
    },
}

def transform(produce):
    if produce['type'] == 'fruit':
        return [color.capitalize() for color in produce['colors']]
    else:
        return produce['size'].upper()

result = [transform(produce) for produce in dict1.values()]

print(result)

# expected
[["Red", "Green"], "MEDIUM", ["Orange"], "LARGE"]

# ! TODO revise
