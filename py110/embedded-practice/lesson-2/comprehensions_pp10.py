"""
A UUID (Universally Unique Identifier) is a type of identifier often used to uniquely identify items,
even when some of those items were created on a different server or by a different application.
That is, without any synchronization, two or more computer systems can create new items and label
them with a UUID with no significant risk of stepping on each other's toes. It accomplishes this
feat through massive randomization. The number of possible UUID values is approximately 3.4 X 10E38, which
is a huge number. The chance of a conflict, a "collision", is vanishingly small with such a large
number of possible values.

Each UUID consists of 32 hexadecimal characters (the digits 0-9 and the letters a-f) represented as a string.
The value is typically broken into 5 sections in an 8-4-4-4-12 pattern,
e.g., 'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'.


Note that our description of UUIDs is a simplified description of how UUIDs are formed.
There are several UUID versions, each with some non-random characteristics in some of the bits.
These different versions can play a part in certain applications.

Write a function that takes no arguments and returns a string that contains a UUID.

I: no param
O: string

Model Solution:
8-4-4-4-12
'f65c57f6-a6aa-17a8-faa1-a67f2dc9fa91'

DS:
Interim: Lists

Algo:
- generate letters a-f store in `hexadecimal_ltr`
- generte numbers 0-9 store in `hexadecimal_num`
- join the two lists to make a combined `hexadecimal`

- initialize a list with the desired lengths in each `places_list`
- iterate iver the `places_list`
    - while the `tiny_list` is less than the first value/equal to maybe?
    `- sample `hexadecimal` and append to `tiny_list`
    - remove the first element of the list

"""
import random

def uuid():
    hexadecimal_chr= 'abcdef0123456789'
    places_list = [8,4,4,4,12]
    uuid = []

    tiny_list = []

    for size in places_list:
        tiny_list = [random.choice(hexadecimal_chr) for _ in range(size)]
        str_chunk = ''.join(tiny_list)
        uuid.append(str_chunk)
    return '-'.join(uuid)
print(uuid())