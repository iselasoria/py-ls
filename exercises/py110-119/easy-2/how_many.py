"""
Write a function that counts the number of occurrences of each element
in a given list. Once counted, print each element alongside the number
of occurrences. Consider the words case sensitive e.g. ("suv" != "SUV").

I: list
O: string

Rules:
- count the number of occurences of each element
- print the element alongside the number of occurences
- case sensitive --> 'suv' != 'SUV'
Model Solution:


DS:
Interim: dictionary

Algo:
- set up an empty dictonary object `dict_tally`

- iterate over the list
    - with each iteartion
        - set the values of each element at 0
        - increment the counter of whatever element is in the `dict_tally`
- print the `dict_tally`

"""

def count_occurrences(lst):
    dict_tally = {}

    for item in lst:
        dict_tally.setdefault(item, 0)
        dict_tally[item] += 1

    for k in dict_tally.keys():
        print(f"{k} => {dict_tally[k]}")


vehicles = ['car', 'car', 'truck', 'car', 'SUV', 'truck',
            'motorcycle', 'motorcycle', 'car', 'truck']

count_occurrences(vehicles)


# expected output

# your output sequence may appear in a different sequence
# car => 4
# truck => 3
# SUV => 1
# motorcycle => 2

