# Write two different ways to remove all of the elements from the following list:

numbers = [1, 2, 3, 4]

# solution 1
numbers.clear()

# solution 2
while numbers:
    numbers.pop()

print(numbers)