"""
Write code that capitalizes the words in the string 'launch school tech & talk',
so that you get the string 'Launch School Tech & Talk'.
"""
phrase = 'launch school tech & talk'


def cap(str):
    w_list = str.split()
    new_list = []

    for word in w_list:
        new_list.append(word.capitalize())

    return ' '.join(new_list)

print(cap(phrase))


# more pythonic

def cap(str):
    return str.title()