"""
Write a function that takes a string argument and returns a
list of substrings of that string. Each substring should
begin with the first letter of the word, and the list
should be ordered from shortest to longest.

I: string
O: list

Rules:
- each substring begins with first letter of the word
- order by substring length ascending

Model Soliution:
abc --> a ab abc --> ['a', 'ab', 'abc']

DS:
list

Algo:
- generate substrings using sliding increasing index


"""



def leading_substrings(str):
    substrings = []
    for sliding_idx in range(len(str)):
        suby = str[:sliding_idx + 1]
        substrings.append(suby)

    return substrings


# All of these examples should print True
print(leading_substrings('abc') == ['a', 'ab', 'abc'])
print(leading_substrings('a') == ['a'])
print(leading_substrings('xyzy') == ['x', 'xy', 'xyz', 'xyzy'])