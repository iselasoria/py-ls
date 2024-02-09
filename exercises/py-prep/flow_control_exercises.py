# 1
# to what values do the expressions evaluate?

False or (True and False) # False
True or (1 + 2) # True
(1 + 2) or True # True
True and (1 + 2) # True
False and (1 + 2) # False
(1 + 2) and True # True
(32 * 4) >= 129 # False
False != (not True) # False
True == 4 # False
False == (847 == '847') # True

# 2
"""Write a function, even_or_odd, that determines whether its argument is an even or odd number. 
If it's even, the function should print 'even'; otherwise, it should print 'odd'. 
Assume the argument is always an integer."""

def even_or_odd(num):

    if num % 2 == 0:
        print('even')
    else:
        print('odd')

even_or_odd(8)

# 3
# without running it, what does the code print and why?

def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113') # Product2 because it finds the '113'
bar_code_scanner(142) # Product not found! because the data type is different, we have '142' in the case but not its int counterpart


# 4
# refactor to use regular if 

#### return ('bar' if foo() else qux())

# becomes.....

# if foo():
#     return 'bar'
# else:
#     return qux()

# 5 what does it output and why?
def is_list_empty(my_list):
    if my_list:
        print('Not Empty')
    else:
        print('Empty')

is_list_empty([]) # Empty--> because the first condition of the if statement would only execute if it returned a trughty value which
# it does not because empty collections are falsey. So, the flow gets yielded to the `else` block and this one executes.

# 6 
"""Write a function that takes a string as an argument and returns an all-caps version of the 
string when the string is longer than 10 characters. Otherwise, it should return the original string. 
Example: change 'hello world' to 'HELLO WORLD', but don't change 'goodbye'."""

def cap_me(str):
    if len(str) > 10:
        return str.upper()
    else:
        return str

print(cap_me('Parangaricutirimicuaro'))
print(cap_me('howdy!'))

# 7

"""
Write a function that takes a single integer argument and prints a message that describes whether:

the value is between 0 and 50 (inclusive)
the value is between 51 and 100 (inclusive)
the value is greater than 100
the value is less than 0
"""

def number_range(num):

    if num < 0:
        print(f'{num} is less than 0')
    elif num <= 50:
        print(f'{num} is between 0 and 50')
    elif num <= 100:
        print(f'{num} is between 51 and 100')
    elif num > 100:
        print(f'{num} is greater than 100')

number_range(0)     # 0 is between 0 and 50
number_range(25)    # 25 is between 0 and 50
number_range(50)    # 50 is between 0 and 50
number_range(75)    # 75 is between 51 and 100
number_range(100)   # 100 is between 51 and 100
number_range(101)   # 101 is greater than 100
number_range(-1)    # -1 is less than 0

