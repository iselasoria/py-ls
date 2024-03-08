# what will this do and why?
a = 1

def my_function():
    a = 2

my_function()
print(a)

# global variable a is initialized and set to 1. The subsequent function definition then assigns a to the integer 2.
# Because we did not use a global keyword, python will treat this as a local varibale and therefore it will have no effect
# on the varibale a as it was defined in the global scope
