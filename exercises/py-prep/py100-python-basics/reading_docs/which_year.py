# The Python documentation for the datetime module provides two attributes to retrieve the year from a date or datetime object: year and isocalendar.


from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]
print(type(today_year))
print(iso_year)

# What is the difference between the year attribute and the isocalendar method?

# the today_year variable points to an integer obj while the iso year points to an element in a tuple containing other elements like week and day 
