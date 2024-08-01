import pprint

def year(book):
    return int(book['published'])

a = sorted(books, key=year)
pprint.pprint(a)




"""

Sort the following list of tuples based on the second element of each tuple, and then by the first element if the second elements are the same.

"""

pairs = [(3, 1), (1, 2), (2, 2), (1, 1), (3, 2)]


def custom_sort(tup):
    return (tup[1], tup[0])

# (3, 1) (1, 2) (2, 2)
# [(1, 1), (3, 1), (1, 2), (2, 2), (3, 2)]
a = sorted(pairs, key=custom_sort)
print(a)