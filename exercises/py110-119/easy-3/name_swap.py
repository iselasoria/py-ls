"""
Write a function that takes a string argument consisting of
a first name, a space, and a last name. The function should
return a new string consisting of the
last name, a comma, a space, and the first name.

I: string
O: string

Rules:
- swap the first and last name
- separate with a comma followed by a space
- assume no middle names, tittles, suffixes, etc.

DS:
Interim: list

Algo:
- split string on the space
- reverse the list
- join the now reversed list with ", " and return

"""
def swap_name(name):
    name_lst = name.split()
    name_lst.reverse()
    return ", ".join(name_lst)
# test cases
print(swap_name('Joe Roberts') == "Roberts, Joe")   # True