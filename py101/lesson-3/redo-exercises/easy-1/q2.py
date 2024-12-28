# how can you determine whether the code ends in an exclamation mark?

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

# SOLUTION
#  use .endswith() method that is available to the string class

print(str1.endswith('!'))
print(str2.endswith('!'))