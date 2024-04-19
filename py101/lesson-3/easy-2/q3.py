"""
Programmatically determine whether 42 lies between 10 and 100, inclusive.
Do the same for the values 100 and 101,
"""

search_num1 = 42
search_num2 = 100
search_num3 = 101

range1 = list(range(10,101))



print(search_num1 in range1)
print(search_num2 in range1)
print(search_num3 in range1)