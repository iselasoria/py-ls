# 1
# write python code to print the seventh number of range(0, 25, 3).

col = list(range(0, 25, 3))
print(col[6])

# 2 
# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.

str = 'Launch School'
my_char = str.find('c')
print(str[my_char:my_char + 6])

# 3
# Write Python code to create a new tuple from (1, 2, 3, 4, 5). The new tuple should be in reverse 
# order from the original. It should also exclude the first and last members of the original. 
# The result should be the tuple (4, 3, 2).
my_tuple = (1, 2, 3, 4, 5)
result = my_tuple[3:0:-1]
print(result)       # (4, 3, 2)

# 3
# three-part question. Consider the following
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

# Part 1: Write some code to print Bark by accessing the element associated with the key Dog.
print(pets['Dog'])

# Part 2: Write some code to print None when you try to print the value associated with the non-existent key, Lizard.
print(pets.get('Lizard'))

# Part 3: Write some code to print <silence> when you try to print the value associated with the non-existent key, Lizard.
print(pets.get('Lizard','<silence>'))

# 5
# which cant be used as a key in a dict and why?
'cat'
(3, 1, 4, 1, 5, 9, 2)
['a', 'b'] # <------- `list`mutable so not usable
{'a': 1, 'b': 2}  # <------- `dict` mutable so not usable
range(5)
{1, 4, 9, 16, 25}  # <------- `set` mutable so not usable
3
0.0
frozenset({1, 4, 9, 16, 25})

# 6
# what will this print?
print('abc-def'.isalpha()) # False
print('abc_def'.isalpha()) # False
print('abc def'.isalpha()) # False
print('abc def'.isalpha() and # False
      'abc def'.isspace())
print('abc def'.isalpha() or
      'abc def'.isspace()) # False
print('abcdef'.isalpha()) # True
print('31415'.isdigit()) # True
print('-31415'.isdigit()) # False
print('31_415'.isdigit()) # False
print('3.1415'.isdigit()) # False
print(''.isspace()) # False


# 7
# Write Python code to replace all the : characters in the string below with +.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

lista = info.split(':')
new_col = '+'.join(lista)
print(new_col)

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
result = info.replace(':', '+')
print(result)
# 'xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh'

# 8
# Explain why the code below prints different values on lines 3 and 4.

text = "It's probably pining for the fjords!"
print(text[21])

print(text[21:35].rfind('f'))     # 8
# this first takes the slice: 'for the fjords!'. From there, it starts now the idx of the substring with the first f at 0, goes up to find the right most istance of the char because ir's rfind.
print(text.rfind('f', 21, 35))    # 29 this does the search between idx 21 and 29, so it begins the reverse find on position 29 and will stop when it finds the first intance of the char, in this case `f`

# 9
# Write some code to replace the value 6 in the following nested list with 606:
stuff = [
    ['hello', 'world'],
    ['example', 'mem', None, 6, 88],
    [4, 8, 12],
]

stuff[1][3] = 606
print(stuff)

# 10 
# consider the following and write one line to list activities Cocoa enjoys

cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            }
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            }
        },
    }
}

print(cats['Pete']['Cocoa']['enjoys'])

# 11 without runing, what shold each print?

print({3, 2} in {1, frozenset({2, 3})}) # True 
print('Joe J' in 'Joe Johnson') # True
print(5 in range(5)) # False
print(5 in range(6)) # True
print(5 not in range(5, 10)) # False
print(4  in {6, 5, 4, 3, 2, 1}) # True
print('johnson' in 'Joe Johnson') # False
print('sen' not in 'Joe Johnson') # True
print(0 in range(10, 0, -1)) # True
print({1, 2, 3} in {1, 2, 3}) # False not true for equality checks

# 12 write some code that determines if the number 3 is found in each of the collections:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

zippped_col = [numbers1, numbers2, numbers3, numbers4, numbers5]
print(zippped_col)

for col in zippped_col:
    if 3 in col:
        print('True')
    else:
        print('False')

# 13
# without running determine what each prints

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')

print('Butterscotch' in cats) # True
print('Butter' in cats) # False; it can't search for substr
print('Butter' in cats[3]) # True; here inside the string, it can search for substr
print('cheddar' in cats) # False

# 14

# assume the following

my_str = 'abc'
my_list = ['Alpha', 'Bravo', 'Charlie']
my_tuple = (None, True, False)
my_range = range(10, 60, 10)

# 15
# Write some code that combines the sequences into a list of tuples. Each tuple should contain one member of each sequence. Print the final result so you can see all the values, which should look like this:

# should look like:
# [('a', 'Alpha', None, 10),
#  ('b', 'Bravo', True, 20),
#  ('c', 'Charlie', False, 30)]

zipped_col = zip(my_str, my_list, my_tuple, my_range)

print(list(zipped_col))