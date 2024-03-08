# what till the following code do and why?

x = 10

def my_function():
    x = x + 5
    print(x)

my_function()

# the varibale x is initialzied and set to the integer 10. Then, the my_function gets defined and inside the body definition
# we set variable x to the result of x + 5 and later call the function. The function will throw an error because Python
# is reading x as a local variable that is getting defined inside the fucntion. Since we attempt to add 5 to its value but this
# is the first time we are assignning it, we will get an error.