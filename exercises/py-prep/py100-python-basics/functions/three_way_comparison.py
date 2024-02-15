# Write a function that compares the length of two strings. It should return -1 
# if the first string is shorter, 1 if the second string is shorter,
#  and 0 if they're of equal length. For example:
# Write a function that compares the length of two strings. It should return -1 if the first string is shorter, 1 if the second string is shorter, and 0 if they're of equal length. For example:

def compare_by_length(str1, str2):
  str1_size = len(str1)
  str2_size = len(str2)

  if str1_size < str2_size:
    return -1
  elif str2_size < str1_size:
    return 1
  else:
    return 0
  


print(compare_by_length('patience', 'perseverance')) # -1
print(compare_by_length('strength', 'dignity') )     #  1
print(compare_by_length('humor', 'grace')   )        #  0