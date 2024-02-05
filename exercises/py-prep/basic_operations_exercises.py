# 1 Concatenate two strings, one with your first name and one with your last, 
# to create a new string with your full name as its value. 
# For example, if your name is John Doe, 
# you should combine 'John' and 'Doe' to get 'John Doe'.

fullname = 'Rosa' + 'Isela'
print(fullname)

# 2 This question may be a little challenging if your math skills are rusty. Don't be afraid to take advantage of the hints. Try your best to solve the problem, but don't feel compelled to complete it if you become frustrated.

# Use the REPL and the arithmetic operators to extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.
# Each digit may require multiple Python statements.
num= 4936

ones = num % 10
print(ones)

num = num // 10 
print(num)

tens = num % 10 
print(tens)

num = num // 10 
print(num)

hund = num % 10 
print(hund)

num = num // 10 
print(num)

thous = num 

# 3 what does this code do and why?
print('5' + '10')

# this code will concatenate the literal strings, so the result will be
# '510. Because the two operands are of the type string, Python will interpret the '+' as
# a concatenation rather than addition. This prduces a new string.

# 4 refactor question 3 to coerce and print 15 instead.
print(int('5') + int('10'))

# 5 
# Will an error occur if you try to access a list element with 
# an index greater than or equal to the list's length? 
# For example:

foo = ['a', 'b', 'c']
print(foo[3])      # will this result in an error?

# this will result in an out of range index error

# 6 
# to what values does the expression evaluate
'foo' == 'Foo'
# this will evaluate to false, Python cares about case adn so the strings are not the same
# casefold method will return a new object of the string class with the chars lowercased
# the casefold() method creates new objects and we can check this by calling id(object_to_check)
# which will return the place in memory

# 7 
# what will the following code do?
int('3.1415')
# this will raise a ValueError.
# the int method exects somethign tht looks already like an integer
# to do that, we first turn it into a float
num = float('3.1415')
result = int(num) # 3.1415
print(result) # 3

# 8
# to what does the expression evaluate?
'12' < '9'
# True because the the operands are strings so Python uses
# char by char comparison and checks first if '1' is less than '9' which
# it is and so since there are no more characters in the second operand,
#  it decides that the first must be smaller than the second