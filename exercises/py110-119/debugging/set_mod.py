"""
We want to remove certain items from a set while iterating
over it, but the code below throws an error. Why is that and
how can we fix it?
"""
data_set = {1, 2, 3, 4, 5}

for item in data_set:
    print(item)
    if item % 2 == 0:
        data_set.remove(item)

# SOLUTION
# it is bad practice to iterate over a collection and change it at the same time
# when we do that here, the 2 gets removed and so 3 is now at index 1,
# but index 1 was already processed, so it wont process again. Now 4 is at index 2
# and it gets removed, so 5 gets pushed there, but index 2 was already processed so
# it wont get processed again