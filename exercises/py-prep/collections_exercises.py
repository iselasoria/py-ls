# 1 
# If you have a list named people, how can you determine the number of entries in that list?
people = ['Joe', 'Anne','Paul']
len(people)


# 2
# Can you write some code to change the value 'bye' in the following tuple to 'goodbye'?

stuff = ('hello', 'world', 'bye', 'now')

# tuples are immuatable, so we can't but the next best thing is:

a = list(stuff)
a[2] = 'goodbye'

print(tuple(a))

# 3 
# Identify at least 2 differences between lists and tuples. Identify at least 2 ways that lists and tuples are similar.

"""
Lists are mutable objects, so we can add and remove elemets destructively. Tuples are immutable. Lists use [] and tuples ().
These two data types are both sequences-- that is, ordered collections. Both of these data types are heterogeneous, they can hold different data types."""

# 4 
# why can we treat strings as sequences?
"""Strings are ordered, and you can access their elements via the index."""

# 5 
# How do the set types differ from the sequence types?
"""Sets are unordered; they dont have indexes."""

# 6 
# aussming the following:
pi = 3.141592

# Write some code that converts the value of pi to a string and assigns it to a variable named str_pi.

str_pi = str(pi)

# 7
# without running the following, identify the numbers that are included in each of the following ranges:
print(list(range(7))) # 0,1,2,3,4,5,6
print(list(range(1, 6))) # 1,2,3,4,5
print(list(range(3, 15, 4))) # 3,7,11
print(list(range(3, 8, -1))) # []
print(list(range(8, 3, -1))) # 8,7,6,5,4

# 8
# how woudl you print all the numbers in the following range?
range(3, 17, 4)

print(list(range(3, 17, 4)))

# 9 
my_list = [1, 2, 3, [4, 5, 6]]
another_list = list(my_list)
# given the code above, answer the following questions and explain your answers: 

"""
Are the lists assigned to my_list and another_list equal? --> the lists are equal in that they contain the same elements
Are the lists assigned to my_list and another_list the same object?--> they have diffrent id so they are different objects.
Are the nested lists at index 3 of my_list and another_list equal? --> yes, the element at the same index is the same on both
Are the nested lists at index 3 of my_list and another_list the same object? --> yes, the elements are the same object. nested collections are subject to shallow copies.
"""



# 10
# Bob expects the following code to print the names in alphabetical order. 
# Without running the code, can you say whether it will? Explain your answer.
names = { 'Chris', 'Clare', 'Karis', 'Karl',
          'Max', 'Nick', 'Victor' }
print(names)

"""
This will not print the names in alphabetical order because sets are unordered collections.If it does, it was done purely at random.
"""

# 11
"""
Name	  Country
Alice	    USA
Francois	Canada
Inti	    Peru
Monika	    Germany
Sanyu	    Uganda
Yoshitaka	Japan



You need to write some Python code to determine the country name associated with one of the listed names. 
Your code should include the data structure(s) you need and at least one test case to ensure the code works.
"""


countries = {
    'Alice':     'USA',
    'Francois':  'Canada',
    'Inti':      'Peru',
    'Monika':    'Germany',
    'Sanyu':     'Uganda',
    'Yoshitaka': 'Japan',
}

print(countries['Inti'])