"""
Write a function that takes a string and returns a dictionary containing the following three properties:

the percentage of characters in the string that are lowercase letters
the percentage of characters that are uppercase letters
the percentage of characters that are neither
All three percentages should be returned as strings whose numeric values lie between "0.00" and "100.00", respectively. Each value should be rounded to two decimal points.

You may assume that the string will always contain at least one character.

I: string
O: ditionary

Rules:
- percentages of characters that are:
    - lowercase
    - uppercase
    - neither
- number to be formatted as string "00.00"- "100.00"
- implicit: white space counts as neither character type

DS:
Inteirm: lists, strings

Algo:
- gen the lenght of the input string 'str_size'

- initi dictionary with the three types: lowercase, uppercase, neither and their valeus set to 0
- iterate over the string
    - with each iteration
        - if the characrter is upper, tally up the coutn in the dict for uppercase
        - if it is lower, tally up lower in dictionary
        - if it is neither, tally up neither
        --> {'lowercase' : 5, 'uppercase' : 2, 'neither' : 3}
- iterate over the dictionary and transformt the value to a percentage, formatted

"""
def pct(count, size):
    return f"{(count/size) * 100:.2f}"

def letter_percentages(stringy):
    str_size = len(stringy)

    sizes_dict = {'lowercase' : 0, 'uppercase' : 0, 'neither' : 0}

    for char in stringy:
        if char.isupper():
            sizes_dict['uppercase'] += 1
        elif char.islower():
            sizes_dict['lowercase'] += 1
        else: sizes_dict['neither'] += 1

    sizes_dict = {k:pct(v,str_size) for k, v in sizes_dict.items() }
    return sizes_dict


expected_result = {
    'lowercase': "50.00",
    'uppercase': "10.00",
    'neither': "40.00",
}
print(letter_percentages('abCdef 123') == expected_result)

expected_result = {
    'lowercase': "37.50",
    'uppercase': "37.50",
    'neither': "25.00",
}
print(letter_percentages('AbCd +Ef') == expected_result)

expected_result = {
    'lowercase': "0.00",
    'uppercase': "0.00",
    'neither': "100.00",
}
print(letter_percentages('123') == expected_result)