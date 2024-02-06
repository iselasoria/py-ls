# 1
"""
Classify the following potential variable names as idiomatic, 
non-idiomatic, or illegal. For the non-idiomatic and illegal names, explain your choice.
"""
index # idiomatic 
CatName #not idiomatic, should not use capital letters
lazy_dog # idiomatic
quick_Fox # non-idiomatic, should not use uppercase letters
1stCharacter # Illegal, should not start with a number
operand2 # idiomatic
BIG_NUMBER #non-idiomatic, all suppercase is used for constants
π # Non-Idiomatic, this is not as ASCII char

# 2
"""
Classify the following potential function names as idiomatic, 
non-idiomatic, or illegal. For the non-idiomatic and illegal names, 
explain your choice.
"""

index # idiomatic
CatName # non-idiomatic, cannot use capitals and should be separated by _
lazy_dog # idiomatic
quick_Fox # non-idiomatic, should not use capitals
1stCharacter # illegal, should not start with a digit
operand2 # idiomatic
BIG_NUMBER # non-idiomatic, call caps reserved for constants
π # non-idiomatic 

# 3
"""
Classify the following potential constant names as idiomatic, 
non-idiomatic, or illegal. For the non-idiomatic and illegal names, 
explain your choice.
"""

index # non-idiomatic, no lowercase
CatName # non-idiomatic, no lowercase
snake_case # non-idiomatic, no lowercase
LAZY_DOG3 # idiomatic
1ST # illegal, can't begin with a digit
operand2 # non-idiomatic, must use caps
BIG_NUMBER # idiomatic
Π # non-diomatic, this is not an ASCII char

# 4
"""
Classify the following potential class names as idiomatic, 
non-idiomatic, or illegal. For the non-idiomatic and illegal names, 
explain your choice.
"""

index # non-idimatic, should not begin with lowercase
CatName # idiomatic
Lazy_Dog # non-idiomatic, should not use underscores
1ST # illegal, cant begin with a digit 
operand2 # non-idiomatic, should not begin with a lowercase
BigNumber3 # idiomatic
Πi # non-idiomatic, not an ASCII char

# 5
"""
Write a program named greeter.py that greets 'Victor' three times. 
Your program should use a variable and not hard code the string value 
'Victor' in each greeting. Here's an example run of the program:
"""

def greeter(name):
    return name
    
print(greeter('Victor'))

print(f"Good morning, {greeter('Victor')}")
print(f"Good afrernoon, {greeter('Victor')}")
print(f"Good evening, {greeter('Victor')}")

# 6
"""
Write a program named age.py that includes someone's age and then 
calculates and reports the future age 10, 20, 30, and 40 years from now. 
Here's the output for someone who is 22 years old.
"""

# def age(num, *timeframe):
#     if timeframe == 10:
#         num += timeframe
#         return num
#     elif timeframe == 20:
#         num += timeframe
#         return num
#     elif timeframe == 30:
#         num += timeframe
#         return num
#     elif timeframe == 40:
#         num += timeframe
#         return num 
#     else:
#         num
        
# print(age(22))

# print(f'You are {age(22)} years old.')
# print(f'In {timeframe}, you will be {age(num, timeframe})')

age = 22
print(f'You are {age} years old.')
print(f'In 10 years, you will be {age + 10} years old.')
print(f'In 20 years, you will be {age + 20} years old.')
print(f'In 30 years, you will be {age + 30} years old.')
print(f'In 40 years, you will be {age + 40} years old.')

# 7
# what happens in the following code, why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# the reassignment works, but it is not advisable to reassign constatns in python

# 8
"""
Assume you have $1,000.00 in the bank, and you've somehow managed to find a bank that pays you 5% (this is a wish-fulfillment fantasy) compounded interest 
every year. After one year, you will have $1,050 
($1,000 times 1.05). After two years, you will have 
$1,050 times 1.05, or $1102.50. Create a variable named balance 
that contains the amount of money you will have after 5 years, 
then print the result. Use a single expression if you can 
to set balance to the correct value.
"""


balance = (1000.00 * 1.05 * 1.05 * 1.05
                   * 1.05 * 1.05)
print(balance)

// TODO  
# 9 
# Repeat the solution using augmented reassignemnt

balance = 1000.00
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
balance *= 1.05
print(balance)

// TODO 
# 10 
"""
Assume that obj already has a value of 42 when the code below 
starts running. Which of the subsequent statements reassign 
the variable? Which statements mutate the value of the object 
that obj references? Which statements do neither? 
If necessary, you can read the documentation.
"""
# starts as:
obj = 42 

obj = 'ABcd'      # Reassignment -> 'ABcd'
obj.upper()       # Neither -> .upper() returns a new value, but we don't capture it
obj = obj.lower() # Reassignment -> 'abcd'
print(len(obj))   # Neither
obj = list(obj)   # Reassignment list() returns a new object, and we then make obj point to it ['a','b','c','d']
obj.pop()         # Mutation -> .pop() mutates the object it is called on ['a','b','c']
obj[2] = 'X'      # Mutation -> this is index reassignment, it may look like reassignment but is is not. Because it acts on and mutates the collection itself ['a','b','c','X']
obj.sort()        # Mutation -> mutatin method, all capitals are greater than all their lowercase counterparts ['X','a','b']
set(obj)          # Neither -> this created a new set ('X','a','b')
obj = tuple(obj)  # Reassignment -> we point the variable to the value of the tuple constructor