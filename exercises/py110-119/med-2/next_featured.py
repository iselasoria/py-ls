"""
A featured number (something unique to this exercise) is an odd number that is a multiple of 7, with all of its digits occurring exactly once each. For example, 49 is a featured number, but 98 is not (it is not odd), 97 is not (it is not a multiple of 7), and 133 is not (the digit 3 appears twice).

Write a function that takes an integer as an argument and returns the next featured number greater than the integer. Issue an error message if there is no next featured number.

NOTE: The largest possible featured number is 9876543201.

I: integer
O: integer

Rule:
- must be multiple 7
- must be odd
- must not have digits occurring more than once
- raise an error if no next featured num


Model Solution:
12 -> 13 -> 14 -> 15 -> 16-> 17-> 18->...21

DS:
int
range
str

Algo:
Helper Funciton:featured_condition(num):
- cast int as string to check for dupes

- if number is multiple of 7 AND odd AND no dupes

Main Function: is_featured(num):
- start iterating from number to ??? 21
    - iteration break when featured numner is found ******
    - if featured is true and not the same as input, then return number at the iteration

"""
HIGHEST_FEATURED = 9876543201

def featured_condition(iteration_var):
    stringy_num = str(iteration_var) # "21"
    duped = len(set(stringy_num)) < len(stringy_num)

    if iteration_var % 7 == 0 and iteration_var % 2 != 0 and not duped:
        return True
    return False

def is_featured(x):
    if x >= HIGHEST_FEATURED:
        return ("There is no possible number that fulfills those requirements.")
    for i in range(x, HIGHEST_FEATURED + 1):
        if featured_condition(i) and i != x:
            return i



# # test cases
print(is_featured(12) == 21)                  # True
print(is_featured(20) == 21)                  # True
print(is_featured(21) == 35)                  # True
print(is_featured(997) == 1029)               # True
print(is_featured(1029) == 1043)              # True
print(is_featured(999999) == 1023547)         # True
print(is_featured(999999987) == 1023456987)   # True
print(is_featured(9876543186) == 9876543201)  # True
print(is_featured(9876543200) == 9876543201)  # True

error = ("There is no possible number that "
         "fulfills those requirements.")
print(is_featured(9876543201) == error)       # True