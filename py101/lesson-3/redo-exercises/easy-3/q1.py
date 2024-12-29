# write two different ways to remove all the elements from teh list:

numbers = [1, 2, 3, 4]

# solution

numbers.clear()

while numbers:
    numbers.pop()

# ! py-quirk check the difference between these two