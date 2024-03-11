"""
Use a for loop to iterate over the numbers dictionary and return a list containing each number divided by 2. 
Assign the returned list to a variable named half_numbers and print its value using print.
"""

numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}

new_list = []
for item in numbers.values():
    new_list.append(item // 2)
print(new_list)