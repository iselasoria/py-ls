# write a fucntion that counts the number of occurences of a substring in a string.
# test cases:

def count_substrings(str, substr):
    return str.count(substr)


print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0