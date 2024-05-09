"""
! TODO revise this one for the edge cases
Write a function that takes a year as input and returns the century.
The return value should be a string that begins with the century number,
and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.

New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.
I:
int

O:
str

Rules:
- begins with century number
- ends with st, nd, rd, th as approriate
- new centuries begin in years that end in 01 for example: 1901-2000 is the 20th century


Algo:
century_num(num):
- if digits is at least 4, then the century is the first two digits + 1 ex: 1802 -> 19th
- if the digits is less than 4, get the closest 100th and round up ex: 245 -> 3rd

sufix(num):
- if the number ends with 1
    - suffix is 'st'
- if the number ends 2
    - suffix is 'nd'
- if it ends with 3
    - suffix is 'rd
- otherwise
    - suffix is 'th'
"""

def century_num(year):
    if (len((str(year))) >= 4) and not str(year).endswith('0'):
        return int(str(year)[:2]) + 1
    elif str(year).endswith('0'):
        return int(str(year)[:2]) - 1
    else:
        return int(str(year - (year % 100))[:1]) + 1

def suffix(centurized_year):
    if str(centurized_year).endswith('1'):
        return 'st'
    elif str(centurized_year).endswith('2'):
        return 'nd'
    elif str(centurized_year).endswith('3'):
        return 'rd'
    elif str(centurized_year).endswith('11') or str(centurized_year).endswith('12') :
        return 'th'
    else:
        return 'th'

def century(year):
    century_format = century_num(year)
    sfx = suffix(century_format)

    return f'{century_format}{sfx}'


# # test cases
# print(century(2000)) #== "20th")          # True
print(century(2001)== "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103)) #== "102nd")        # True
print(century(1052)) #== "11th")          # True
print(century(1127))# == "12th")          # True
print(century(11201))# == "113th")        # True