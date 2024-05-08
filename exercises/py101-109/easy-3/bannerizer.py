"""
Write a function that takes a short line of text and prints it within a box.

I:
string

O:
string

Algo:
- print the corner plus the '-' for the length of the srting + 2 for padding and add anothjer corner
- print an empty line with just borders
- print the borders with padding and message
- repeat the empty line
- repeat the first border line

"""

def print_in_box(msg):
    edge = '+' + ('-' * (len(msg) + 2)) + '+'
    emt = '|' + (' ' * (len(msg) + 2))  + '|'

    print(edge)
    print(emt)
    print('| ' + msg + ' |')
    print(emt)
    print(edge)


"""
test cases :

print_in_box('To boldly go where no one has gone before.')

+--------------------------------------------+
|                                            |
| To boldly go where no one has gone before. |
|                                            |
+--------------------------------------------+


print_in_box('')

+--+
|  |
|  |
|  |
+--+
"""
print_in_box('To boldly go where no one has gone before.')
print_in_box('')