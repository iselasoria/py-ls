# Using the official Python documentation, can you determine how to check whether a string contains a specific substring?

str ='Onomatoxelapeia'
name = 'Xela'

print(str.find(name.casefold()))

print(name.casefold() in str)