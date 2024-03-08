# what will it print and why?
a = 1

def my_function():
    print(a)

my_function()

# global variable a is set to integer 1
# a function is deinfed that makes a call to print with a passed in as an argument
# Lastly, the my_funtion method gets called. Because the variable a is intialzied as a global variable, it is accessible 
# inside the method definition as well. So this code will output 1. 
# we can't reassign or make changes to a without using the global keyword but we can refrence it