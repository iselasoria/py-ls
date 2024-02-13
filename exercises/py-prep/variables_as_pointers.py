# 1 In your own words, explain the difference between the two expressions:

my_object1 == my_object2 # <--- this is checking for equality. When true, this means the objects these variables point to have the same values
my_object1 is my_object2 # <-- this is checking for identify. When true, this means the objects these variables point to _are_ the same object


#  2 
# Without running, what will the code print and why?
set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

# sets are mutable. On line two, we initialize `set2` and 
# point to to the object referenced by the variable `set1`, 
# we then modify the first set by adding elements to it. Line 4 should print 
{42, 'Monty Python', ('a', 'b', 'c'), range(5,10)} 
# since the second set is referencing the same object that set1 points to at the time of the 
# mutation


# 3 without running whart wilol it print and why?
dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1) # this initializes a new object
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python']) # The Life of Brian


# 4 
# without runing, what will it print and why?
dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1) # this initializes a new object
dict1['a'][1] = 42
print(dict2['a']) # [1, 42, 3]

# Thedictionaries are different objects, but they share value components since the `dict` constructor creates a shallow copy.
# TODO

# 5 
# Write some code to create a deep copy of the dict1 object and assign it to dict2. You should only modify the code where indicated.


import copy

dict1 = {
    'a': [[7, 1], ['aa', 'aaa']],
    'b': ([3, 2], ['bb', 'bbb']),
}

dict2 = copy.deepcopy(dict1)# You may modify the `???` part
            # of this line

# All of these should print False
print(dict1         is dict2)
print(dict1['a']    is dict2['a'])
print(dict1['a'][0] is dict2['a'][0])
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])



# 6 
"""
The following program is nearly identical to that of the previous exercise.
However, this time, it should create a shallow copy of dict1. 
Be careful: you're not allowed to use the copy module in this exercise.`

In addition, before you run this code, can you predict the output values?
"""


dict1 = {
    'a': [{7, 1}, ['aa', 'aaa']],
    'b': ({3, 2}, ['bb', 'bbb']),
}

dict2 = dict(dict1) # You may modify the `???` part
            # of this line

print(dict1         is dict2) 
print(dict1['a']    is dict2['a']) 
print(dict1['a'][0] is dict2['a'][0]) 
print(dict1['a'][1] is dict2['a'][1])
print(dict1['b']    is dict2['b'])
print(dict1['b'][0] is dict2['b'][0])
print(dict1['b'][1] is dict2['b'][1])

## Python's constructors for collections all craete 
# shallow copies. So here we use the `dict` constructor. The first print False because they are not the same obj. The rest, since they are shallow copies all reference the original objects. 
##### Deep copies are different objects altogether, shallow copies re-use some elements in the original objects. ####

