"""
A double number is an even-length number whose left-side digits
are exactly the same as its right-side digits.
For example, 44, 3333, 103103, and 7676 are all double numbers,
whereas 444, 334433, and 107 are not.

Write a function that returns the number provided as an argument
multiplied by two, unless the argument is a double number.
If the argument is a double number, return the double number as-is.

I:
int

O:
int

Rules:
- double doubles are returned as is
- return the inpiut number multiples by 2 if it is not a double double
* double doubles would have to be even length

Algo:
if the number is not even length, multiple by 2
else return number
"""
def twice(num):
    dd = str(num)
    half = len(dd) // 2

    return num * 2 if dd[:half] != dd[half:] else num


# test cases
print(twice(37)== 74)                  # True
print(twice(44)== 44)                  # True
print(twice(334433)== 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103)== 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676)== 7676)              # True