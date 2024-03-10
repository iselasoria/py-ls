# write a function that checks whether the string  starts with a specifc prefix
def starts_with(word, prefix):
    p_size = len(prefix)
    word_chunk = word[:p_size]

    return prefix == word_chunk


# test cases
print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True