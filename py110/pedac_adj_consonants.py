"""## Algo:
- initialize an empty dictionary `consonant_tally`
- iterate over the input list ['can can', 'toucan', 'batman', 'salt pan']
- with every iteration
    - initialize a string object `adj_cons_in_word`  # 'can can'
    - iterate over the string characters # c,a,n, ,c,a,n
        - push character to `adj_cons_in_word` IF the last char in the variable is also consonant
    - write to the `consonant_tally`
        - word as key
        - the length of `adj_cons_in_word` as value
"""
#! TODO

def consonant(ltr):
    return ltr not in 'AEIOU aeiou'



def sort_by_consonant_count(lst):
    consonant_tally = {}

    for word in lst:
        consonant_tally.setdefault(word, 0)
        copy_word = ''
        adj_cons_word = ''

        for idx, ch in enumerate(word):
            copy_word += ch
            print(f'Current char: {ch} and previous char: {copy_word[idx - 1]}')

            # print(word[idx-1])
            if consonant(ch) and consonant(copy_word[-1]): #and consonant(adj_cons_word[-1]):
                adj_cons_word += ch
                consonant_tally[word] += 1

    result = list(consonant_tally.keys())
    return result




# test cases

# my_list = ['aa', 'baa', 'ccaa', 'dddaa']
# print(sort_by_consonant_count(my_list))
# # ['dddaa', 'ccaa', 'aa', 'baa']

my_list = ['can can', 'toucan', 'batman', 'salt pan']
print(sort_by_consonant_count(my_list))
# ['salt pan', 'can can', 'batman', 'toucan']

# my_list = ['bar', 'car', 'far', 'jar']
# print(sort_by_consonant_count(my_list))
# # ['bar', 'car', 'far', 'jar']

# my_list = ['day', 'week', 'month', 'year']
# print(sort_by_consonant_count(my_list))
# # ['month', 'day', 'week', 'year']

# my_list = ['xxxa', 'xxxx', 'xxxb']
# print(sort_by_consonant_count(my_list))
# # ['xxxx', 'xxxb', 'xxxa']