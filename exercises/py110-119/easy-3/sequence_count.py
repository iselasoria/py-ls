"""
Create a function that takes two integers as arguments.
The first argument is a count, and the second is the starting
number of a sequence that your function will create.
The function should return a list containing the same number
of elements as the count argument. The value of each element
should be a multiple of the starting number.

You may assume that count will always be an integer greater
than or equal to 0. The starting number can be any integer.
If the count is 0, the function should return an empty list.

I: two integers--> count, starting point
O: list

Rules:
- resulting list should have the length indicated by the coutn arg
- each element should be a multiple of the second arg
- assume always positive numbers
- if the count is 0, return empty list

DS:
Interim: list

Algo:
- initialize a results list to hold the result
- iterate over an enumerated range that goes from starting_point and stops at starting_point + count - 1 --> [-7, ]
- with each iteartion
    - multiply the starting_point times the variable in the current iteration


"""

def sequence(count, starting_point):
    result = []

    for idx, item in enumerate(range(starting_point, starting_point + (count + 1))):
        if idx > 0:
            result.append(starting_point * idx)

    return result
# test cases
print(sequence(5, 1) == [1, 2, 3, 4, 5])          # True
print(sequence(4, -7) == [-7, -14, -21, -28])     # True
print(sequence(3, 0) == [0, 0, 0])                # True
print(sequence(0, 1000000) == [])                 # True