# how can you determine if a string ends with an exclamation mark
# write some code that prints True or False depending on
# whether the string ends with an exclamation mark

str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

print(str1.endswith('!'))
print(str2.endswith('!'))

# using the last index
print(str1[-1] == '!')
print(str2[-1] == '!')