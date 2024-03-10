# Write an is_empty_or_blank function to determine whether a string is 
# either empty or consists entirely of spaces. For example:

# def is_empty_or_blank(str):
#     str_mod = str.strip()
#     return len(str_mod) == 0

# more pythonic 

def is_empty_or_blank(str):
    return len(str.strip()) == 0

print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True