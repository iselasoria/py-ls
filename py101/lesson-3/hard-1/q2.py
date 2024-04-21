"""
What does the last line in the code output?
"""
dictionary = {'first': [1]}
num_list = dictionary['first']
num_list.append(2)

print(num_list)
print(dictionary)

# the outputs, respectively, will be:
[1, 2]
{'first': [1, 2]}

# since append is a mutating function, when we pass the dictionary object we are
# passing a referene to the original object, and this append will modify the original
# if we just want to modify the num_list and not the original, we can make a copy
dictionary = {"first": [1]}
num_list = dictionary["first"].copy()
num_list.append(2)

# we could also use slicing whic creates a new object
dictionary = {"first": [1]}
num_list = dictionary["first"][:]
num_list.append(2)