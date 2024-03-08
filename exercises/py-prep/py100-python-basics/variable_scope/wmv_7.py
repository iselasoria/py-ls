# what will this do and why?

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)

# global variabel a is initalzied and set to integer 1.
# Inside the function definition, we use global keyword on the varibale a, so now we are referencing the a defined in 
# the global scope, and we have the ability to alter it. The on the next line we do just that-- we reassign it to the integer 2
# then we call the function, so by the time we print it we are referncing the newly altered a which is pointing to integer 2
 