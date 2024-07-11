"""
A developer is trying to remove duplicates from a list.
They use a set for deduplication, but the order of elements
is lost. How can we preserve the order?
"""
data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = list(set(data))
print(unique_data == [4, 2, 1, 3]) # order not guaranteed

data = [4, 2, 4, 2, 1, 3, 2, 3, 2, 4, 3]
unique_data = []
seen = set()

for item in data:
    if item not in seen:
        seen.add(item)
        unique_data.append(item)

print(unique_data == [4, 2, 1, 3]) # True

# ? Practice this cosntructor over and over; chunking
# SOLUTION
# this solution uses the set constructor as a funnel to get the de-duplicates
# but it is dumping data into a list as it iterates which is preserving the order
