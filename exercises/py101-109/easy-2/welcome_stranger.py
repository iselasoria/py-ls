"""
Create a function that takes 2 arguments, a list and a dictionary.
The list will contain 2 or more elements that, when joined with spaces,
will produce a person's name. The dictionary will contain two keys,
"title" and "occupation", and the appropriate values.
Your function should return a greeting that uses the person's full name,
and mentions the person's title.

I:
- list
- dictionary


Rules:
- list includes all parts of the person's name, when joined with spaces

Algo:
- return a greeting for the person using full name and occupation

"""

def greetings(name_list, job):
    full_name = ' '.join(name_list)
    return f'Hello {full_name}! Nice to have a {job["title"]} {job["occupation"]}'

print(greetings( ["John", "Q", "Doe"], {"title": "Master", "occupation": "Plumber"},))
# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# # Hello, John Q Doe! Nice to have a Master Plumber around.