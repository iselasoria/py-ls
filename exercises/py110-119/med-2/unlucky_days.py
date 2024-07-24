"""
Some people believe that Fridays that fall on the 13th day of the
month are unlucky days. Write a function that takes a year as an
argument and returns the number of Friday the 13ths in that year.
You may assume that the year is greater than 1752, which is when
the United Kingdom adopted the modern Gregorian Calendar. You may
also assume that the same calendar will remain in use for the
foreseeable future.


"""

import datetime

def friday_the_13ths(year):
    thirteenths = [datetime.date(year, month, 13) for month in range(1,13)] # this gives all the 13ths of the month

    unlucky_fridays = 0
    for day in thirteenths:
        if day.weekday() == 4: # day of the week starts 0Monday to 6Sunday
            unlucky_fridays += 1

    return unlucky_fridays


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True