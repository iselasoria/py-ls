# what will this output?

my_list1 = [{"first": "value1"}, {"second": "value2"}, 3, 4, 5]
my_list2 = my_list1.copy()
my_list2[0]['first'] = 42
print(my_list1)

# solution
# on the second line, we are making a copy of the object referenced by my_list1 and storin that in my_list2
# using the copy method creates a shallow copy, which we must rememeber, does not make copies of the nested objects,
# in this case, the list itself is a copy, buyt the eleement sin the list are shared.
# thus, when we then alter the object using indexed assignment and subsequently, reassingment with a key for a dictionary,
# we are acting on the original nested objects, albeit, through the copied list. So, by the time we print my_list1,
# we can expect to get
[{'first': 42}, {'second': 'value2'}, 3, 4, 5]