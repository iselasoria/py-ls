"""
Write a function that takes two arguments, a string and a positive integer,
then prints the string as many times as the integer indicates.
"""
def repeat(str, times):
   for t in range(times):
      print(str)

# test cases
repeat('Hello', 3)