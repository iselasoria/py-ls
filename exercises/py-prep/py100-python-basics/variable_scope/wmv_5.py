# what will the code do and why?
a = 1

def my_function():
    print(a)
    a = 2

my_function()

"""
variable a is initialized and set to integer 1, then my_function gets defined and  inside the body definition, 
it calls print with a passed in as an argument. The next line then attempts to reassign a to the integer 2. 
Line 5, the call to print with a as the argument would work as use a with the value 1 as it comes in from global. The 
issue is that since in the next line we attempt reassignment, python treats a now as a local varibale instead of a global
For this reason, we will get an error thrown because we are attempting to reference a local variable a with a value of 2, 
one line before we even define it.
"""