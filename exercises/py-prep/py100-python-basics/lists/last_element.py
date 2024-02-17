# Write a function that returns the last element of a list provided as an argument. 
# be sure to handle the empty arguments.

def last(lst):
    if lst:
        return lst[-1]
# For example:
print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([]))

