#  Extract keys where all values in their lists are odd numbers.

lst = [
    {'a': [1, 3, 5]},
    {'b': [2, 4, 6], 'c': [3, 5], 'd': [4]},
    {'e': [7], 'f': [9, 11]},
]

# Compute and display the total age of employees in the 'IT' department.
employees = {
    'Alice':  {'age': 29,  'department': 'HR'},
    'Bob':    {'age': 35,  'department': 'IT'},
    'Charlie': {'age': 28, 'department': 'Marketing'},
    'David':   {'age': 42, 'department': 'IT'},
    'Eve':     {'age': 25, 'department': 'HR'},
}


# Filter dictionaries where at least one value list is empty.

lst = [
    {'a': [1, 2, 3], 'b': []},
    {'c': [2, 4], 'd': [3, 6]},
    {'e': [], 'f': [6, 10]},
]

# write a function to retrieve the names of all the managers in the company

company = {
    "engineering": [
        {"name": "Alice", "age": 29, "position": "developer"},
        {"name": "Bob", "age": 32, "position": "developer"},
        {"name": "Charlie", "age": 37, "position": "manager"}
    ],
    "hr": [
        {"name": "Dave", "age": 41, "position": "recruiter"},
        {"name": "Eve", "age": 36, "position": "manager"}
    ],
    "sales": [
        {"name": "Frank", "age": 28, "position": "salesperson"},
        {"name": "Grace", "age": 34, "position": "manager"}
    ]
}
