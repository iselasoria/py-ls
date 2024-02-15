# How many arguments does the str.join method expect? What happens if you call it with fewer or more arguments?

# str.join takes exacrtlt one argument, if we supply less than or more than that it will raise an error
str = 'XELA'

print('----'.join(str))

# X----E----L----A
# basically, the string object it gets called on becoems the separator, 
# while the iterator we pass is the collections whose elememts will be 
# separated by the separator