# you come across this code, what errors does it raise for the given examples and what do they mean?

def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n

find_first_nonzero_among(0, 0, 1, 0, 2, 0) 
find_first_nonzero_among(1)

# SOLUTION: this raises an error because we are passig more arguments than there are parameters defined. The 
# the body of the function tells us we should be passing a list
