"""
Given the following code, what will the final values of a and b be?
Try to answer without running the code.
"""
a = 2
b = [5, 8]
lst = [a, b]

lst[0] += 2 # 4
lst[1][0] -= a # 1

# a still points to 2 because we modified the list object, we didnt reference `a`
# since `b` is a list and we are modoifuing that list by assigning a new value at index 0, the value of `b` does change
# ! todo
