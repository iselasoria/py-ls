# what will this code do?
a = 7

def my_function(b):
    b += 10

my_function(a)
print(a)

# global variable a is initialized and sett ot integer 7
# then, the function definition sates it should take an argument. insside the body defintion, we take the parameter b and add 10
# the call to my_function with a passed in as the argument will update the value of the local variable b to 17, but this does not 
# affect the value referenced by global a
# In python, integers are immutable so the fact that we referenced the value of global a via another variable (the b argument), had
# no effect on the actual value of the global variable
