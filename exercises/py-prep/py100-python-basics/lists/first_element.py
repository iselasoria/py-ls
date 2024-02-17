
# Write a function that returns the first element of a list provided as an argument. 
# Be sure to handle the case where the input list is empty.


def first(lst):
   if lst:
      return lst[0]

# For example:
print(first(['Earth', 'Moon', 'Mars']))  # Earth
print(first([]))  # Earth

