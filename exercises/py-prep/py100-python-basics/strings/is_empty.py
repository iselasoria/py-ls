# write a functionm that checks whtehr s string is empty ot not. For example:

def is_empty(str):
    if len(str) == 0:
        return True
    else:
        return False
    
# simpliefied version of the above:
def is_empty(str):
    return len(str) == 0

# more pythonic solution:

def is_empty(str):
    return not str

print(is_empty('mars'))  # False
print(is_empty('  '))    # False
print(is_empty(''))      # True